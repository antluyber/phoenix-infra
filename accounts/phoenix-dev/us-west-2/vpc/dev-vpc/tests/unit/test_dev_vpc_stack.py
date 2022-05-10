import aws_cdk as core
import aws_cdk.assertions as assertions

from dev_vpc.dev_vpc_stack import DevVpcStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dev_vpc/dev_vpc_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DevVpcStack(app, "dev-vpc")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
