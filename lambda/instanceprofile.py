import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()['Reservations']
    instances_with_roles = []
    for reservation in instances:
        for instance in reservation['Instances']:
            if 'IamInstanceProfile' in instance:
                instances_with_roles.append(instance['InstanceId'])
    return instances_with_roles
