#!/usr/bin/env python3
import os

import aws_cdk as cdk
from dotenv import dotenv_values
from aws_health_mon.aws_health_mon_stack import AwsHealthMonStack

config_file = os.environ.get("CONFIG", ".env")
config = dotenv_values(config_file)

app = cdk.App()

stack_name = config.get("stack_name", "AwsHealthMonStack")

AwsHealthMonStack(app, stack_name, config)

app.synth()
