
# AWS Heath Monitoring

This project creates a service to poll the AWS health API in your AWS account on a regular interval and post updates to a slack incoming webhook.
The health api is only available to Business, or Enterprise support plan accounts. For more details see the [aws health user guide](https://docs.aws.amazon.com/health/latest/ug/health-api.html#using-the-python-code). We use a polling pattern to be able to pick up `public` events that do not trigger as cloudwatch events natively.
We use CDK to create and deploy the infrastructure for the service, which is comprised of a lambda to poll the api, eventbridge rule to trigger the lambda and several permissions and policies. We've created the option to automatically query the api in other accounts given a list of arns for assumable roles kept in secrets manager. 

## Configure and Bootstrap

The CDK stack has a few possible configuration items passed in via environment variables or a `.env` file:

- `slack_secret` this is name of a secrets manager secret containing the webhook url you wish to publish to (Default: 'health_status_slack_url')
- `frequency` the interval in minutes to poll the api for (Default: 5 minutes)
- `accts_secret` list of arns for assumable roles in additional accounts (Default: "")
  
You must prestage a slack webhook url into secret manager in the same region where your stack will be deployed it should have the format:

- secret key: "url"
- secret value: "https://hooks.slack.com/services/foo/bar"
  
either name the secret `health_status_slack_url` or update a `.env` file with the name of the secret. 

If you wish to make cross account calls you need to creaet a secret in secrets manager with the format:

- secret key: 'arns'
- secret value: "arn1,arn2,arn3"

And then add the name of the secret to your environment variables or `.env` file. 

Note: You also must bootstrap the account for cdk deployment if you have not already:

```bash
cdk bootstrap
```

## Build and Deploy

We've included a [Taskfile](https://github.com/adriancooney/Taskfile) to simplify the setup, build and deploy of this cdk project. Taskfile is like a makefile but is natively a set of shell functions, and doesnt require any special dependencies.

## Initial Setup

```bash
./Taskfile setup
```

This will create the virtualenv for python, install the dependencies for cdk and the lambda, and then create the lambda layer .zip file. 

## Deploy

```bash
./Taskfile deploy
```

This will do a synthesis of the cdk stack and attempt to deploy it to the account your are currently logged into.
