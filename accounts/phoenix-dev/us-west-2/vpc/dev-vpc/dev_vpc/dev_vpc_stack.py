from typing import Mapping
from constructs import Construct
from aws_cdk import (
    App,
    # Duration,
    CfnOutput,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_logs as logs,
    aws_route53resolver as route53resolver
)
from constructs import Construct

class DevVpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # Create the VPC Resource
        service_name = scope.node.try_get_context('serviceName')
        dns_log_retention_days=14

        self.vpc = ec2.Vpc(self, "FFDevVPC",
                            cidr="10.0.0.0/16",
                            max_azs=2,
                            nat_gateways=1,
                            subnet_configuration=[
                                ec2.SubnetConfiguration(
                                    subnet_type=ec2.SubnetType.PUBLIC,
                                    name="public-subnet",
                                    cidr_mask=24,
                                    map_public_ip_on_launch=False,
                                ),
                                ec2.SubnetConfiguration(
                                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                                    name="private-subnet-nat",
                                    cidr_mask=24
                                ),
                                ec2.SubnetConfiguration(
                                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                                    name="isolated-subnet",
                                    cidr_mask=24
                                ) 
                            ]
                    )

        # Create VPC Flow Logs log group
        self.vpc_flow_log_group = logs.LogGroup(self, 'Dev-FlowLogsLogGroup',
            log_group_name=service_name,
            retention=logs.RetentionDays('ONE_YEAR')
        )

        # Setup IAM role for logs
        self.role = iam.Role(self, 'Dev-FlowLogsRole',
            assumed_by=iam.ServicePrincipal('vpc-flow-logs.amazonaws.com')
        )
        
        # VPC Flow Log
        self.vpc_log = ec2.FlowLog(self, 'Dev-VPCFlowLogs',
            resource_type=ec2.FlowLogResourceType.from_vpc(self.vpc),
            destination=ec2.FlowLogDestination.to_cloud_watch_logs(self.vpc_flow_log_group, self.role)
        )

        # DNSLogs LogGroup
        self.route53_logs = logs.LogGroup(self, 'Dev-DNSQueryLogGroup',
            log_group_name='dev-dns-logs',
            retention=logs.RetentionDays('TWO_WEEKS')
        )

        self.cfn_resolver_query_logging_config = route53resolver.CfnResolverQueryLoggingConfig(self, "MyCfnResolverQueryLoggingConfig",
            destination_arn=self.route53_logs.log_group_arn,
            name="dev-route53-query-logging"
        )

        self.cfn_resolver_query_logging_config_association = route53resolver.CfnResolverQueryLoggingConfigAssociation(self, "MyCfnResolverQueryLoggingConfigAssociation",
            resolver_query_log_config_id=self.cfn_resolver_query_logging_config.attr_id,
            resource_id=self.vpc.vpc_id
        )

        CfnOutput(self, "Output",
                  value=self.vpc.vpc_id
        )
