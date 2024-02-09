#!/usr/bin/env python3

import sys
import subprocess
import json
import logging

# Function to install boto3 and import it
def install_and_import_boto3():
    try:
        import boto3
    except ImportError:
        print("boto3 not found, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "boto3"])
        import boto3
    return boto3

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def list_buckets(s3_client):
    try:
        response = s3_client.list_buckets()
        return [bucket['Name'] for bucket in response['Buckets']]
    except Exception as e:
        logger.error("Error listing buckets: %s", e)
        sys.exit(1)

def update_bucket_acl(s3_client, bucket_names, acl_setting):
    for bucket_name in bucket_names:
        try:
            s3_client.put_bucket_acl(
                ACL=acl_setting,
                Bucket=bucket_name
            )
            logger.info(f"Bucket {bucket_name} ACL updated to {acl_setting}.")
        except Exception as e:
            logger.error("Error updating ACL for %s: %s", bucket_name, e)

def update_bucket_policy(s3_client, bucket_names, policy_json):
    for bucket_name in bucket_names:
        try:
            s3_client.put_bucket_policy(
                Bucket=bucket_name,
                Policy=policy_json
            )
            logger.info(f"Bucket policy updated for {bucket_name}.")
        except Exception as e:
            logger.error("Error updating policy for %s: %s", bucket_name, e)

def confirm_action(message):
    confirmation = input(message + " (yes/no): ")
    return confirmation.lower() == 'yes'

def main():
    boto3 = install_and_import_boto3()
    s3_client = boto3.client('s3')

    bucket_names = list_buckets(s3_client)
    logger.info("Buckets found: %s", bucket_names)

    print("\nChoose the bucket(s) to update:")
    print("1. Update a single bucket")
    print("2. Update all buckets")
    bucket_choice = input("Enter your choice (1 or 2, or 'exit' to quit): ")

    if bucket_choice.lower() == 'exit':
        print("Exiting.")
        return

    selected_buckets = []
    if bucket_choice == "1":
        print("\nSelect a bucket by its number:")
        for i, bucket_name in enumerate(bucket_names, start=1):
            print(f"{i}. {bucket_name}")
        bucket_index = input("Enter the bucket number (or 'exit' to quit): ")

        if bucket_index.lower() == 'exit':
            print("Exiting.")
            return

        try:
            index = int(bucket_index) - 1
            selected_buckets.append(bucket_names[index])
        except (ValueError, IndexError):
            logger.error("Invalid bucket selection. Exiting.")
            return
    elif bucket_choice == "2":
        selected_buckets = bucket_names
    else:
        logger.error("Invalid bucket choice. Exiting.")
        return

    print("\nChoose the ACL setting for the selected bucket(s):")
    print("1. Public Read")
    print("2. Public Read & Write")
    acl_choice = input("Enter your choice (1 or 2, or 'exit' to quit): ")

    if acl_choice.lower() == 'exit':
        print("Exiting.")
        return

    acl_setting = ""
    if acl_choice == "1":
        acl_setting = "public-read"
    elif acl_choice == "2":
        acl_setting = "public-read-write"
    else:
        logger.error("Invalid ACL choice. Exiting.")
        return

    if confirm_action(f"Are you sure you want to set {acl_setting} for selected bucket(s)?"):
        update_bucket_acl(s3_client, selected_buckets, acl_setting)

    # Sample policy - Replace with the appropriate policy as per your need
    sample_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{selected_buckets[0]}/*"
            }
        ]
    }
    policy_json = json.dumps(sample_policy)

    if confirm_action(f"Are you sure you want to apply a new policy to selected bucket(s)?"):
        update_bucket_policy(s3_client, selected_buckets, policy_json)
    else:
        print("Action canceled. Exiting.")

if __name__ == "__main__":
    main()