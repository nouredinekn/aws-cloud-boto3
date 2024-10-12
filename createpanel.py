import boto3

# Initialize a session using your root credentials
a = input('aws_access_key_id: ')
b = input('aws_secret_access_key: ')
session = boto3.Session(
    aws_access_key_id=a,
    aws_secret_access_key=b,
    region_name='us-east-1'  # Change to your desired region
)

# Create IAM client
iam_client = session.client('iam')

# Define the user name and password
user_name = 'AdminUser'
password = 'YuanDima@A12'  # Set the password for AWS Management Console login
admin_policy_arn = 'arn:aws:iam::aws:policy/AdministratorAccess'

# Create a new IAM user
try:
    iam_client.create_user(UserName=user_name)
    print(f"User {user_name} created successfully.")
except iam_client.exceptions.EntityAlreadyExistsException:
    print(f"User {user_name} already exists.")

# Attach the 'AdministratorAccess' policy to the new user
iam_client.attach_user_policy(
    UserName=user_name,
    PolicyArn=admin_policy_arn
)
print(f"AdministratorAccess policy attached to {user_name}.")

# Create a login profile for console access
iam_client.create_login_profile(
    UserName=user_name,
    Password=password,
    PasswordResetRequired=False  # Set to True if you want the user to reset password on first login
)
print(f"Login profile with password set for {user_name}.")

# Create access keys for the new user
response = iam_client.create_access_key(UserName=user_name)
access_key = response['AccessKey']
access_key_id = access_key['AccessKeyId']
secret_access_key = access_key['SecretAccessKey']

# Get the user's ARN
user_details = iam_client.get_user(UserName=user_name)
user_arn = user_details['User']['Arn']

# Write user credentials to a file
with open('AIM-USER.txt', 'a') as f:
    f.write(f"https://{user_arn.split('/')[0]}.signin.aws.amazon.com/console|{user_name}|{password}|{access_key_id}|{secret_access_key}\n")

print(f"Credentials written to AIM-USER.txt: {access_key_id}, {secret_access_key}")
