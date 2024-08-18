import boto3
import time

# Create a Lightsail client

client = boto3.client('lightsail', region_name='ap-northeast-1')

# Define the instance configuration
instance_config = {
    'instanceNames': ['my-windows-instance'],
    'availabilityZone': 'ap-northeast-1a',
    'blueprintId': 'windows_server_2022',
    'bundleId': 'xlarge_win_3_0',  # Use the bundle ID for "Xlarge"
    'userData': '#ps1\nnet user Administrator MyPassword123!',
    'tags': [{'key': 'Name', 'value': 'MyWindowsInstance'}]
}

# Create the instance
response = client.create_instances(**instance_config)

# Get the instance name from the configuration
instance_name = instance_config['instanceNames'][0]

# Wait for the instance to be in the running state
instance = None
while not instance or instance['state']['name'] != 'running':
    time.sleep(5)
    instance = client.get_instance(instanceName=instance_name)

# Get the public IP address of the instance

public_ip = instance['publicIpAddress']

# Print instance information
print("Instance Name:", instance_name)
print("Public IP address:", public_ip)
print("Username: Administrator")
print("Password: MyPassword123!")
