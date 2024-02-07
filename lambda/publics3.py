import boto3
import json
from botocore.exceptions import ClientError

# Global variable to track bucket states
previous_public_buckets = set()

def lambda_handler(event, context):
    global previous_public_buckets

    # Initialize AWS services
    s3 = boto3.client('s3')
    sns = boto3.client('sns')
    current_public_buckets = set()

    print("Starting to check all S3 buckets for public access...")

    try:
        buckets = s3.list_buckets()['Buckets']
        print(f"Total buckets found: {len(buckets)}")

        for bucket in buckets:
            bucket_name = bucket['Name']
            print(f"Checking bucket: {bucket_name}")

            try:
                # Check ACL
                acl = s3.get_bucket_acl(Bucket=bucket_name)
                for grant in acl['Grants']:
                    if 'AllUsers' in grant['Grantee']:
                        current_public_buckets.add(bucket_name)
                        print(f"Bucket {bucket_name} is public via ACL.")

                # Check Bucket Policy
                policy = s3.get_bucket_policy(Bucket=bucket_name)
                if 'Public' in policy['Policy']:
                    current_public_buckets.add(bucket_name)
                    print(f"Bucket {bucket_name} is public via Policy.")
            
            except ClientError as e:
                print(f"Error checking bucket {bucket_name}: {e}")

    except ClientError as e:
        print(f"Error listing buckets: {e}")

    # Find newly public buckets
    new_public_buckets = current_public_buckets - previous_public_buckets
    print(f"Newly public buckets since last check: {new_public_buckets}")

    # Update previous_public_buckets with the current state
    previous_public_buckets = current_public_buckets

    # Alert if new public buckets found
    if new_public_buckets:
        alert_message = f"Newly public buckets found: {', '.join(new_public_buckets)}"
        print(alert_message)

        try:
            sns_response = sns.publish(
                TopicArn='arn:aws:sns:us-east-1:571355216739:s3BucketMonitor',
                Message=alert_message,
                Subject='Newly Public S3 Bucket Alert'
            )
            print(f"SNS alert sent. Response: {sns_response}")
        except ClientError as e:
            print(f"Error sending SNS alert: {e}")

    print("Lambda function execution completed.")
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda execution completed')
    }
