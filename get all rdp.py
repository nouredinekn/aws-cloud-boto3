import boto3

# Create a Lightsail client
lightsail_regions = [
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
    "ap-south-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "sa-east-1"
]

for i in lightsail_regions:
    try:
        client = boto3.client('lightsail', region_name=i)
        # List all instances
        instances = client.get_instances()

        # Iterate through instances and print RDP access details
        for instance in instances['instances']:
            instance_name = instance['name']
            public_ip = instance.get('publicIpAddress', 'N/A')
            state = instance['state']['name']
            print(f"region name: {i}")
            print(f"Instance Name: {instance_name}")
            print(f"Public IP Address: {public_ip}")
            print(f"State: {state}")
            
            if public_ip != 'N/A':
                print(f"RDP Address: {public_ip}")
            
            print("=" * 30)
    except:
        pass
