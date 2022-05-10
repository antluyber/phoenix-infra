import aws_cdk as core
import aws_cdk.assertions as assertions

from dev_fargate_lb_cluster.dev_fargate_lb_cluster_stack import DevFargateLbClusterStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dev_fargate_lb_cluster/dev_fargate_lb_cluster_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DevFargateLbClusterStack(app, "dev-fargate-lb-cluster")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
