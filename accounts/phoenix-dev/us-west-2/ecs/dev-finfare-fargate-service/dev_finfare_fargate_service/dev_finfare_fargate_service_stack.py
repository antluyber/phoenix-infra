from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    App, CfnOutput, Stack, Duration
)
from constructs import Construct


print('fargate')
class DevFinfareFargateServiceStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        cluster_name = "DevFargateLbClusterStack-ecsCluster15812518-fFXhOJWEdWGC"
        vpc=ec2.Vpc.from_lookup(self, "vpc", region='us-east-1', vpc_id='vpc-01ea18e30b47b58f3')
        #security_group = ""

        # The cluster where this service should run
        cluster = ecs.Cluster.from_cluster_attributes(
            self, "Cluster",
            vpc=vpc,
            cluster_name=cluster_name,
            #security_groups=[
                #ec2.SecurityGroup.from_security_group_id(
                    #self, "SecurityGroup",
                    #security_group_id=security_group
                #)
            #]
        )

        # Create Fargate Service
        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "MyFargateService",
            cluster=cluster,            # Required
            cpu=512,                    # Default is 256
            desired_count=2,            # Default is 1
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
            ),
            memory_limit_mib=2048,      # Default is 512
            public_load_balancer=True   # Default is False
        )

        fargate_service.service.connections.security_groups[0].add_ingress_rule(
            peer = ec2.Peer.ipv4(vpc.vpc_cidr_block),
            connection = ec2.Port.tcp(80),
            description="Allow http inbound from VPC"
        )

        # Setup AutoScaling policy
        #scaling = fargate_service.service.auto_scale_task_count(
            #max_capacity=2
        #)
        #scaling.scale_on_cpu_utilization(
            #"CpuScaling",
            #target_utilization_percent=50,
            #scale_in_cooldown=Duration.seconds(60),
            #scale_out_cooldown=Duration.seconds(60),
        #)

        CfnOutput(
            self, "LoadBalancerDNS",
            value=fargate_service.load_balancer.load_balancer_dns_name
        )

#app = App()
#AutoScalingFargateService(app, "aws-fargate-application-autoscaling")
#DevApp1FargateServiceStack(app, "aws-fargate-application-autoscaling")
#app.synth()
