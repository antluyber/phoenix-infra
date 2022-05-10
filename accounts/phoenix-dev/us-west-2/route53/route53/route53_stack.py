from aws_cdk import (
    Stack, aws_cloudwatch as cloudwatch,
    aws_route53 as route53
)
from constructs import Construct

class Route53Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hosted_zone = route53.HostedZone(self, "MyHostedZone", zone_name="finfare.com")
        metric = cloudwatch.Metric(
            namespace="AWS/Route53",
            metric_name="DNSQueries",
            dimensions_map={
                "HostedZoneId": hosted_zone.hosted_zone_id
            }
    )

