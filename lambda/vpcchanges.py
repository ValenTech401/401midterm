import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    vpcs = ec2.describe_vpcs()['Vpcs']
    vpc_changes = [vpc for vpc in vpcs if vpc['IsDefault'] is False]
    return vpc_changes
