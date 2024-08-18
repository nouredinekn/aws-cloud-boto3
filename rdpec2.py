import boto3

# Create an EC2 client
ec2_client = boto3.client('ec2', region_name='us-east-1')

# Define the instance configuration
instance_config = {
    'ImageId': 'ami-09301a37d119fe4c5',
    'InstanceType': 'c5.4xlarge',
    'KeyName': 'my-key-pair',
    'UserData': '#ps1\nnet user Administrator MyPassword123!',
    'MinCount': 1,
    'MaxCount': 1,
    'TagSpecifications': [
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'MyWindowsInstance'}]
        }
    ]
}

# Launch the EC2 instance
instances = ec2_client.run_instances(**instance_config)['Instances']

# Get the instance ID
instance_id = instances[0]['InstanceId']

# Wait for the instance to be in the running state
ec2_client.get_waiter('instance_running').wait(InstanceIds=[instance_id])

# Describe the instance to get its information
instance = ec2_client.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]

# Get the public IP address of the instance
public_ip = instance.get('PublicIpAddress', 'N/A')

# Print instance information
print("Instance ID:", instance_id)
print("Public IP address:", public_ip)
print("Username: Administrator")
print("Password: MyPassword123!")
