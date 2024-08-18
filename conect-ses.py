import boto3

def check_ses_quota(aws_access_key_id, aws_secret_access_key, region_name):
    ses_client = boto3.client(
        'ses',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    try:
        response = ses_client.get_send_quota()
        return {region_name: response['Max24HourSend']}
    except Exception as e:
        return {region_name: '0.00', 'error': str(e)}

if __name__ == '__main__':
    aws_access_key_id = input('Access key: ')
    aws_secret_access_key = input('Secret key: ')
    region_name = input('Region: ')
    
    result = check_ses_quota(aws_access_key_id, aws_secret_access_key, region_name)
    print(result)
