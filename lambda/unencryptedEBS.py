import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    volumes = ec2.describe_volumes()['Volumes']
    unencrypted_volumes = [v['VolumeId'] for v in volumes if not v['Encrypted']]
    return unencrypted_volumes
