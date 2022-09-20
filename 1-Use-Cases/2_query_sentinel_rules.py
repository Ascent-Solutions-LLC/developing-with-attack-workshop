import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.securityinsight import SecurityInsights
from dotenv import load_dotenv


# Do a bunch of stuff to connect to Azure
load_dotenv()


SUBSCRIPTION_ID = os.environ["SUBSCRIPTION_ID"]
RESOURCE_GROUP_NAME = os.environ["RESOURCE_GROUP_NAME"]
WORKSPACE_NAME = os.environ["WORKSPACE_NAME"]


# Use the Default Azure Credential (via something like `az login`)
credential = DefaultAzureCredential(exclude_visual_studio_code_credential=True)

# create a Security Insights Client
security_insights_client = SecurityInsights(credential, SUBSCRIPTION_ID)

# create a Rule Templates Client
alert_rules_template_client = security_insights_client.alert_rule_templates

# Get all of the Rule Templates
rule_templates = alert_rules_template_client.list(RESOURCE_GROUP_NAME, WORKSPACE_NAME)

# Get the first template
example_rule_template = list(rule_templates)[0]

# Print the details
print(example_rule_template.name)
print(example_rule_template.description)
print(example_rule_template.tactics)
print(example_rule_template.techniques)
