# read the workflow template
WORKFLOW_TEMPLATE=$(cat .github/workflow-template.yml)
ACCT_REGION="accounts/finfare-dev/us-east-1"

# iterate each route in routes directory
for SERVICE in $(ls $ACCT_REGION); do
	echo "generating workflow for service/${SERVICE}"

	# replace template route placeholder with route name
	WORKFLOW=$(echo "${WORKFLOW_TEMPLATE}" | sed "s/{{SERVICE}}/${SERVICE}/g")
	
	# save workflow to .github/workflows/{SERVICE}
	echo "${WORKFLOW}" > .github/workflows/${SERVICE}.yml
done