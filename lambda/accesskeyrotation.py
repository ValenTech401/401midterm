import boto3
from datetime import datetime, timezone

def lambda_handler(event, context):
    iam = boto3.client('iam')
    users = iam.list_users()['Users']
    old_keys = []
    for user in users:
        access_keys = iam.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']
        for key in access_keys:
            create_date = key['CreateDate']
            age = (datetime.now(timezone.utc) - create_date).days
            if age > 90:
                old_keys.append(key['AccessKeyId'])
    return old_keys
