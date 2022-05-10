from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    App, Stack, Environment, CfnOutput
)
from constructs import Construct

class DevECSCluster(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        existing_vpc=ec2.Vpc.from_lookup(self, "vpc", region='us-west-2', vpc_id='vpc-0776dd759cd9b4793')

        cluster = ecs.Cluster(
            self, 'dev-ecsCluster',
            cluster_name='dev-finfare-ecs-cluster',
            enable_fargate_capacity_providers=True,
            vpc=existing_vpc
        )

