import boto3

def lambda_handler(event, context):
    cloudtrail = boto3.client('cloudtrail')
    trails = cloudtrail.describe_trails()['trailList']
    trail_status = {trail['Name']: cloudtrail.get_trail_status(Name=trail['TrailARN'])['IsLogging'] for trail in trails}
    return trail_status
