import boto3

def lambda_handler(event, context):
    rds = boto3.client('rds')
    instances = rds.describe_db_instances()['DBInstances']
    public_instances = [i['DBInstanceIdentifier'] for i in instances if i['PubliclyAccessible']]
    return public_instances
