import boto3
from botocore.exceptions import NoCredentialsError

# Configuration
API_KEY = "SECRETS"
SECRET_KEY = "SECRETS"
BUCKET_NAME = "employee"
REGION = "Tokyo"  # e.g., "us-east-1"

# Initialize the S3 client
def initialize_s3_client(api_key, secret_key, region):
    return boto3.client(
        's3',
        aws_access_key_id=api_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )

# Upload a file to S3
def upload_file_to_s3(s3_client, file_path, bucket_name, s3_key):
    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f"File {file_path} uploaded successfully to {bucket_name}/{s3_key}")
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except NoCredentialsError:
        print("Credentials not available.")

# Main function
def main():
    # Initialize S3 client
    s3_client = initialize_s3_client(API_KEY, SECRET_KEY, REGION)

    # File details
    file_path = "path/to/your/local/file.txt"  # Replace with your file's local path
    s3_key = "your/desired/s3/key/file.txt"  # Replace with the desired S3 key

    # Upload file to S3
    upload_file_to_s3(s3_client, file_path, BUCKET_NAME, s3_key)

if __name__ == "__main__":
    main()
