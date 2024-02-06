import boto3

def lambda_handler(event, context):
    route53 = boto3.client('route53')
    domains = route53.list_domains()['Domains']
    transferable_domains = [domain['DomainName'] for domain in domains if domain['TransferLock'] is False]
    return transferable_domains
