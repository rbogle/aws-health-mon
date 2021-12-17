#!/usr/bin/env python3
import os

import aws_cdk as cdk
from dotenv import dotenv_values
from aws_health_mon.aws_health_mon_stack import AwsHealthMonStack


app = cdk.App()
config = dotenv_values(".env")

AwsHealthMonStack(app, "AwsHealthMonStack", config)

app.synth()
