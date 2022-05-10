#!/usr/bin/env python3
import os

import aws_cdk as cdk

from dev_finfare_fargate_service.dev_finfare_fargate_service_stack import DevApp1FargateServiceStack

aws_account=os.getenv("CDK_DEFAULT_ACCOUNT", "497928199462") # Default is dev account
aws_region=os.getenv("CDK_DEFAULT_REGION", "us-west-2")
 
app = cdk.App()
DevApp1FargateServiceStack(app, "DevApp1FargateServiceStack", env=cdk.Environment(
    account=aws_account,
    region=aws_region
)

app.synth()
