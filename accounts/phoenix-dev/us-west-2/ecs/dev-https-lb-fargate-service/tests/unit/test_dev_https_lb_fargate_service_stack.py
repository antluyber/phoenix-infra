import aws_cdk as core
import aws_cdk.assertions as assertions

from dev_https_lb_fargate_service.dev_https_lb_fargate_service_stack import DevHttpsLbFargateServiceStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dev_https_lb_fargate_service/dev_https_lb_fargate_service_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DevHttpsLbFargateServiceStack(app, "dev-https-lb-fargate-service")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
