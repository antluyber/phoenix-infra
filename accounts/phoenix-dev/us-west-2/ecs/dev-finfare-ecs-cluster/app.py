#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import App, Stack

from dev_finfare_ecs_cluster.dev_finfare_ecs_cluster_stack import DevECSCluster

app = App()

# hardcoded for dev account
aws_account=os.getenv("CDK_DEFAULT_ACCOUNT", "497928199462") # Default is dev account
aws_region=os.getenv("CDK_DEFAULT_REGION", "us-west-2")
tags={"app_name": "dev-ecs-cluster"}
dev_usw2 = cdk.Environment(account=aws_account, region=aws_region)

DevECSCluster(app, "DevECSCluster", env=dev_usw2)
app.synth()

