import boto3
from US_Visa_Prediction.constants import (
    AWS_SECRET_ACCESS_KEY_ENV_KEY,
    AWS_ACCESS_KEY_ID_ENV_KEY,
    AWS_REGION_ENV_KEY,
)


class S3Client:

    s3_client = None
    s3_resource = None

    def __init__(self):
        self.access_key_id = AWS_ACCESS_KEY_ID_ENV_KEY
        self.secret_access_key = AWS_SECRET_ACCESS_KEY_ENV_KEY
        self.region_name = AWS_REGION_ENV_KEY
        """ 
        This Class gets aws credentials from env_variable and creates an connection with s3 bucket 
        and raise exception when environment variable is not set
        """

        if S3Client.s3_resource == None or S3Client.s3_client == None:
            if self.access_key_id is None:
                raise Exception(
                    f"Environment variable: {self.access_key_id} is not not set."
                )
            if self.secret_access_key is None:
                raise Exception(
                    f"Environment variable: {self.secret_access_key} is not set."
                )

            S3Client.s3_resource = boto3.resource(
                "s3",
                aws_access_key_id=self.access_key_id,
                aws_secret_access_key=self.secret_access_key,
                region_name=self.region_name,
            )
            S3Client.s3_client = boto3.client(
                "s3",
                aws_access_key_id=self.access_key_id,
                aws_secret_access_key=self.secret_access_key,
                region_name=self.region_name,
            )
        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client
