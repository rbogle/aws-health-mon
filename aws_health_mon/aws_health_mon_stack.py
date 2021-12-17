from typing import Dict,Any
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,
    aws_secretsmanager as sm,
    
)
from constructs import Construct

class AwsHealthMonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, config: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        frequency_minutes = config.get("frequency", "5")
        schedule_expression = f"{frequency_minutes} minutes" # type: str
        accounts_secret_name = config.get("accts_secret", "") # type: str
        slack_secret_name = config.get("slack_secret", "health_status_slack_url") # type: str
        accounts = None
        
        # retrieve accounts secret with arns for assuming roles x-account
        if accounts_secret_name != "":
            accounts_secret = sm.Secret.from_secret_name_v2(self, "acct-secret", accounts_secret_name)
            accounts  = accounts_secret.secret_value.to_string().split(',')

        slack_secret = sm.Secret.from_secret_name_v2(self, "slack-secret", slack_secret_name)

        # add deps layer for lambda
        deps_layer = _lambda.LayerVersion(
            self,
            id="lambda-powertools",
            code=_lambda.Code.from_asset("./layers/deps-layer.zip")
        )

        # lambda to poll the health-api and post to slack
        health_api_poll = _lambda.Function(
            self,
            id='health-api-poller',
            runtime=_lambda.Runtime.PYTHON_3_9,
            layers=[deps_layer],
            code=_lambda.Code.from_asset("./lambdas"),
            handler="health.handle_request",
            environment={
                "POLL_INTERVAL": frequency_minutes,
                "SLACK_SECRET": slack_secret_name,
                "ACCOUNTS_SECRET": accounts_secret_name
            }
        )
        
        # give lambda permission to retrieve secret 
        secrets_policy = iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["secretsmanager:GetSecretValue"],
            resources=[slack_secret.secret_arn]
        )

        # give the lambda permissions to assume roles in other account
        # and lookup the arns in secrets manager 
        if accounts is not None:
            assume_policy = iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["sts.AssumeRole"],
            )
            for acct in accounts:
                assume_policy.add_resources(acct)

            secrets_policy.add_resources(accounts_secret.secret_arn)
            health_api_poll.add_to_role_policy(assume_policy)

        # add the secrets policy too
        health_api_poll.add_to_role_policy(secrets_policy)

        # Eventbridge rule to execute on schedule
        polling_rule = events.Rule(
            self,
            id="polling-rule",
            schedule=events.Schedule.expression(schedule_expression)
        )
        # Add the lambda as a target for the rule execution
        polling_rule.add_target(
            targets.LambdaFunction(health_api_poll)
        )
        
