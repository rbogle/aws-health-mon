from typing import Any, Dict, Tuple
import aws_lambda_powertools as alp
import requests
import os
import boto3
from datetime import date, datetime,timezone,timedelta
from aws_lambda_powertools.utilities.parameters import get_secret
from slack_sdk.webhook import WebhookClient


# globals
log_level = os.environ.get("LOG_LEVEL", "INFO")
time_delta = float(os.environ.get("POLL_INTERVAL", 5))
secrets_name = os.environ.get("ACCOUNTS_SECRET")
accounts = list()
logger = alp.Logger("health-poller", level=log_level)
slack_url = get_secret(os.environ.get("SLACK_SECRET", "health_status_slack_url"), transform="json")['url']
slack_client = WebhookClient(slack_url)

# list of assumable role arns kept in secrets_manager
if secrets_name:
    accounts = get_secret(secrets_name,transform='json').get("arns").split(",")

accounts.insert(0,"")

# will return a health api client for an account given an assumable role. 
def health_api_client(rolearn: str="") -> Tuple[boto3.client, str]:
    client = None
    alias = ""
    if rolearn !="":
        sts = boto3.client("sts")
        acct = sts.assume_role(RoleArn=rolearn, RoleSessionName="cross-account-health")
        client = boto3.client("health",
            aws_access_key_id = acct['Credentials']['AccessKeyId'],
            aws_secret_access_key = acct['Credentials']['SecretAccessKey'],
            aws_session_token = acct['Credentials']['SessionToken']
        )
        alias = boto3.client("iam",
            aws_access_key_id = acct['Credentials']['AccessKeyId'],
            aws_secret_access_key = acct['Credentials']['SecretAccessKey'],
            aws_session_token = acct['Credentials']['SessionToken']
        ).list_account_aliases()['AccountAliases'][0]
    else:
        client = boto3.client("health")
        alias = boto3.client("iam").list_account_aliases()['AccountAliases'][0]
    return ( client , alias)

# get a datetime object representing an interval in the past
def get_past_time(minutes_interval: float=5) -> datetime:
    return datetime.now(timezone.utc)- timedelta(minutes=minutes_interval) 

def post_slack_msg(client: WebhookClient, event: dict, account: str ):
    event_description = event['eventDescription'].get('latestDescription')
    event_region = event['event'].get('region')
    event_status = event['event'].get('statusCode') # type: str
    event_service = event['event'].get('service', 'UNKNOWN').title()
    event_type = " ".join(event['event'].get('eventTypeCode','AWS_SERVICE_UNKNOWN').split('_')[2:]).title() # AWS_SERVICE_DESCRIPTION
    event_category = event['event'].get('eventTypeCategory').title() # issue | accountNotification | scheduledChange | investigation
    emoji = ":warning:"
    if event_status == "closed":
        emoji = ":white_check_mark:"

    msg_blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"{emoji} *AWS {event_service} {event_type}*"
            }
        },
        {
            "type": "divider",
        },
        {
			"type": "section",
			"text":                 {
					"type": "mrkdwn",
					"text": f"*{event_category} is _{event_status.upper()}_*"
				}, 
		},
        {
            "type": "divider",
        },
		{
			"type": "context",
			"elements": [

                {
					"type": "mrkdwn",
					"text": f"*{account}*"
				}, 
                {
					"type": "mrkdwn",
					"text": f"*{event_region}*"
				}, 

    
            ]
        },

        {
            "type": "divider",
        },
        		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": event_description
			}
		}
    ]
    client.send(text= f"{emoji} *AWS {event_service} {event_type}*",blocks=msg_blocks)

def get_recent_events( from_time: datetime, assume_role_arn: str="", event_type: str="") -> Tuple[list,str]:
    # get creds for an accounts health api 
    health, account_name = health_api_client(assume_role_arn) # 
    my_filter = {
        'lastUpdatedTimes': [ 
            { 'from': str(from_time) }
        ]
    }
    if event_type !="":
        my_filter['eventTypeCategories']= event_type
    response= health.describe_events(
        maxResults = 100,
        filter = my_filter
    ) # type: Dict[str,Any]
    
    recent_changes = response.get('events', list())
    # get arns of returned events
    recent_arns = list()
    for event in recent_changes:
        recent_arns.append(event.get('arn'))
    # get event details
    if recent_changes:
        response = health.describe_event_details(eventArns=recent_arns)
    return (response.get('successfulSet', list()), account_name)

# lambda request handler
@logger.inject_lambda_context(log_event=True)
def handle_request(event: Dict[str,Any], context: Dict[str,Any]):

    since_time = get_past_time(time_delta)
    # query this account's health-api for any event
    # that has been updated in the last x mintues
    for arn in accounts:
        events, acct_name = get_recent_events(since_time, assume_role_arn=arn)
        for event in events:
            post_slack_msg(slack_client, event, acct_name)
    