import boto3

# Create an IAM client using the default credential provider chain
conn = boto3.client('iam')

def main():
    try:
        user_response = conn.list_users()
        users = user_response['Users']
    
        for user in users:
            user_name = user['UserName']
            user_a_key_response = conn.list_access_keys(UserName=user_name)
            access_keys = user_a_key_response['AccessKeyMetadata']

            for a_key in access_keys:
                if a_key['Status'] == 'Active':
                    print(f"User: {user_name} -> Access Key: {a_key['AccessKeyId']} created on {a_key['CreateDate']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
