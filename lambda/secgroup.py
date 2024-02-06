import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    security_groups = ec2.describe_security_groups()['SecurityGroups']
    open_security_groups = []
    for sg in security_groups:
        for rule in sg['IpPermissions']:
            if '0.0.0.0/0' in str(rule['IpRanges']):
                open_security_groups.append(sg['GroupId'])
    return open_security_groups
