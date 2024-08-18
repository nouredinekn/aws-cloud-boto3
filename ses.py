import boto3
#ses 200 check
def get_ses_limits():
    # List of all AWS regions
    regions = [
        "ap-south-1", "eu-north-1","us-east-1", "eu-west-3", "eu-west-2", "eu-west-1",
        "ap-northeast-3", "ap-northeast-2", "ap-northeast-1", "ca-central-1",
        "sa-east-1", "ap-southeast-1"
    ]
    
    for region in regions:
        print(f"Region: {region}")
        
        # Create a Boto3 SES client for the region
        ses_client = boto3.client("ses", region_name=region)
        
        # Get SES sending limits
        response = ses_client.get_send_quota()
        
        if "Max24HourSend" in response and "MaxSendRate" in response and "SentLast24Hours" in response:
            max_24_hour_send = response["Max24HourSend"]
            max_send_rate = response["MaxSendRate"]
            sent_last_24_hours = response["SentLast24Hours"]
            
            print("Sending Quota:")
            print(f"  Max 24-hour send: {max_24_hour_send}")
            print(f"  Max Send rate: {max_send_rate}")
            print(f"  Sent Last 24 Hours: {sent_last_24_hours}")
            print("----------------------")
        else:
            print("Sending quota information not available.")
            print("----------------------")

if __name__ == "__main__":
    get_ses_limits()
