import boto3

def get_ec2_vcpu_limit(region):
    # Create a Boto3 Service Quotas client for the specified region
    service_quotas_client = boto3.client('service-quotas', region_name=region)

    # Define the service and quota code for EC2 vCPUs
    service_code = 'ec2'
    quota_code = 'L-1216C47A'

    # Get the EC2 vCPUs quota value
    response = service_quotas_client.get_service_quota(
        ServiceCode=service_code,
        QuotaCode=quota_code
    )

    if 'Quota' in response and 'Value' in response['Quota']:
        vcpu_limit = response['Quota']['Value']
        return vcpu_limit
    else:
        return None

def main():
    # List of all AWS regions
    regions = [
        "us-east-1", "us-west-1", "us-west-2", "eu-west-1", "eu-central-1",
        "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ap-northeast-2",
        "sa-east-1"
    ]

    for region in regions:
        vcpu_limit = get_ec2_vcpu_limit(region)
        if vcpu_limit is not None:
            print(f"Region: {region}, vCPUs Limit: {vcpu_limit}")
        else:
            print(f"Region: {region}, vCPUs Limit information not available.")

if __name__ == "__main__":
    main()
