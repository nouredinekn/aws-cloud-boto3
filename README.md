

# AWS Cloud Boto3 Project

This project provides a set of scripts and tools for managing AWS services using the Boto3 library in Python. It is designed to simplify interactions with various AWS resources, allowing users to automate tasks, manage configurations, and interact with AWS services effectively.

## Features

- **EC2 Management**: Create, terminate, and manage EC2 instances.
- **IAM User Management**: Create and manage IAM users, roles, and permissions.
- **CloudFormation Management**: Deploy and manage AWS CloudFormation stacks.
- **SES Management**: Send emails using Amazon Simple Email Service (SES).

## Scripts

The following scripts are included in the project:

1. **`connect-ses.py`**: Connects to Amazon Simple Email Service (SES) for sending and managing emails.
2. **`datecreate.py`**: Creates resources based on the current date. Use this for time-sensitive automation.
3. **`ec2.py`**: Manages EC2 instances, including launching, terminating, and listing instances.
4. **`get all rdp.py`**: Retrieves all RDP (Remote Desktop Protocol) configurations from specified instances.
5. **`rdpec2.py`**: Manages RDP sessions with EC2 instances.
6. **`rdplighstail.py`**: Manages RDP sessions with AWS Lightsail instances.
7. **`ses.py`**: Provides additional SES functionality, including sending emails and managing configurations.

## Requirements

To run this project, you need:

- Python 3.x
- Boto3 library
- AWS account with appropriate permissions

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/nouredinekn/aws-cloud-boto3.git
   cd aws-cloud-boto3
   ```

2. **Install required packages**:

   You can install the required libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials**:

   Ensure that your AWS credentials are configured. You can do this using the AWS CLI or by creating a `~/.aws/credentials` file with the following format:

   ```plaintext
   [default]
   aws_access_key_id = YOUR_ACCESS_KEY
   aws_secret_access_key = YOUR_SECRET_KEY
   region = YOUR_AWS_REGION
   ```

## Usage

Each script serves a specific purpose. You can execute them individually from the command line. For example:

- To connect to SES, run:

  ```bash
  python connect-ses.py
  ```

- To create resources based on the current date, run:

  ```bash
  python datecreate.py
  ```

- To manage EC2 instances, run:

  ```bash
  python ec2.py
  ```

- To get all RDP configurations, run:

  ```bash
  python get all rdp.py
  ```

- To manage RDP sessions with EC2, run:

  ```bash
  python rdpec2.py
  ```

- To manage RDP sessions with Lightsail, run:

  ```bash
  python rdplighstail.py
  ```

- For additional SES functionalities, run:

  ```bash
  python ses.py
  ```

Refer to the individual script comments for more details on how to use each functionality.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue. You can also fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - for detailed API reference.
- [AWS Documentation](https://docs.aws.amazon.com/index.html) - for information on various AWS services.

## Contact

For any inquiries or feedback, feel free to reach out:

- Telegram: [@nouredine_kn](https://t.me/nouredine_kn)
