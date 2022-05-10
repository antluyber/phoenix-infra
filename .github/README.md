

# Cloud Infra
## Cloud Infra
Use this repository to create AWS Services and Resources for shared use amongst different accounts

### Create a Directory Structure

accounts/<account_name>/<region_name>/<service_name>/<app_name>

### Example
To create an ECR Repo to host docker images for finfare app in the dev account us-east-1 region

```
  mkdir -p accounts/finfare-dev/us-east-1/ecr/finfare
  cd accounts/finfare-dev/us-east-1/ecr/finfare
  cdk init --language python
  # Activate your Python virtual environment
  # NOTE: For Windows users, replace with ".env\Scripts\activate.bat"
  source .env/bin/activate
  # Install CDK Python general dependencies
  pip install -r requirements.txt
  # Install CDK Python ECS dependencies
  pip install aws_cdk.aws_ec2 aws_cdk.aws_ecs aws_cdk.aws_ecr aws_cdk.aws_iam
