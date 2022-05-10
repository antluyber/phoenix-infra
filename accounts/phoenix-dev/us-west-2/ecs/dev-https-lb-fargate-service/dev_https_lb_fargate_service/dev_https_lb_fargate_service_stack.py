from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    CfnOutput, Stack, Duration
)
from aws_cdk.aws_route53 import HostedZone
from aws_cdk.aws_certificatemanager import Certificate
from aws_cdk.aws_elasticloadbalancingv2 import SslPolicy
from constructs import Construct

class DevHttpsLbFargateServiceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, props, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # vpc: ec2.Vpc
        # cluster: ecs.Cluster

        aws_region=props['region']
        certificate = Certificate.from_certificate_arn(self, "Cert", "arn:aws:acm:us-east-1:497928199462:certificate/cb6a4706-7f6c-44c5-a20f-af16bccb2f55")
        domain_zone = HostedZone.from_lookup(self, "Zone", domain_name="finfare.com")
        my_vpc_id=props['vpc_id']
        vpc=ec2.Vpc.from_lookup(self, "vpc", region=aws_region, vpc_id=my_vpc_id)

        #cluster = ecs.Cluster(self, "dev-ecs-cluster", vpc=vpc)

        load_balanced_fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(self, "Service",
            vpc=vpc,
            #cluster=cluster,
            certificate=certificate,
            ssl_policy=SslPolicy.RECOMMENDED,
            domain_name="api.finfare.com", 
            domain_zone=domain_zone, 
            redirect_http=True, 
            memory_limit_mib=1024, 
            cpu=512,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
            )
        )

        load_balanced_fargate_service.target_group.configure_health_check(
            path="/custom-health-path"
        )
