# network access control list

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    nacls = ec2.describe_network_acls()['NetworkAcls']
    changed_nacl_ids = []

    for nacl in nacls:
        # Check for any recent changes in the NACL entries
        # This is a simplified check; you might want to implement a more robust comparison
        # depending on your specific requirements.
        for entry in nacl['Entries']:
            if entry['Egress'] == False and (entry['RuleAction'] == 'allow' or entry['RuleAction'] == 'deny'):
                changed_nacl_ids.append(nacl['NetworkAclId'])

    return changed_nacl_ids
