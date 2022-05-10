#!/usr/bin/env python3
import os

import aws_cdk as cdk

from dev_https_lb_fargate_service.dev_https_lb_fargate_service_stack import DevHttpsLbFargateServiceStack

aws_account=os.getenv('CDK_DEFAULT_ACCOUNT', '497928199462')
aws_region=os.getenv('CDK_DEFAULT_REGION', 'us-west-2')
vpc_id='vpc-0776dd759cd9b4793'

props = {'namespace': 'FargateStack ', 'vpc_id': vpc_id, 'region': aws_region, 'account': aws_account}

app = cdk.App()
DevHttpsLbFargateServiceStack(app, "DevHttpsLbFargateServiceStack", props,
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    env=cdk.Environment(account=aws_account, region=aws_region),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
