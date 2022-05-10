import aws_cdk as core
import aws_cdk.assertions as assertions

from route53.route53_stack import Route53Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in route53/route53_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Route53Stack(app, "route53")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
