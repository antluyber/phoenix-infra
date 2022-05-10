from aws_cdk import (
    Stack,
    aws_ecr as ecr,
)
from constructs import Construct

class DevEcrStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ecr_repository = ecr.Repository(self, "dev-ecr")