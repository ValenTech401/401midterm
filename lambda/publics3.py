import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    public_buckets = []
    for bucket in buckets:
        try:
            acl = s3.get_bucket_acl(Bucket=bucket['Name'])
            for grant in acl['Grants']:
                if 'AllUsers' in grant['Grantee']:
                    public_buckets.append(bucket['Name'])
        except ClientError as e:
            print(e)
    return public_buckets
