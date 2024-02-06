import boto3
import json

def lambda_handler(event, context):
    iam = boto3.client('iam')
    policy_changes = []
    for record in event['Records']:
        if record['eventName'] in ['CreatePolicy', 'DeletePolicy', 'UpdatePolicy']:
            policy_changes.append(record)
    return policy_changes
