import aws_cdk as core
import aws_cdk.assertions as assertions

from dev_ecr.dev_ecr_stack import DevEcrStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dev_ecr/dev_ecr_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DevEcrStack(app, "dev-ecr")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
