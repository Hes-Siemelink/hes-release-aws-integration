from digitalai.release.integration import BaseTask

import boto3


class CreateS3Bucket(BaseTask):
    """
        Fetches product details from a remote server
    """

    def execute(self) -> None:

        # Process input
        server = self.input_properties['server']
        if server is None:
            raise ValueError("Server field cannot be empty")
        endpoint_url = server['url']
        bucket = self.input_properties['bucketName']

        # Make request
        s3_client = boto3.client('s3', endpoint_url=endpoint_url, region_name='eu-west-2',
                              aws_access_key_id="", aws_secret_access_key="")

        response = s3_client.create_bucket(Bucket=bucket)

        self.set_output_property('location', response['Location'])


class ListS3Buckets(BaseTask):
    """
        Fetches product details from a remote server
    """

    def execute(self) -> None:

        # Process input
        server = self.input_properties['server']
        if server is None:
            raise ValueError("Server field cannot be empty")
        endpoint_url = server['url']

        # Make request
        s3_client = boto3.client('s3', endpoint_url=endpoint_url, region_name='eu-west-2',
                              aws_access_key_id="", aws_secret_access_key="")

        response = s3_client.list_buckets()

        # Example response: [{'CreationDate': datetime.datetime(2023, 4, 21, 15, 13, 35, tzinfo=tzutc()), 'Name': 'new-bucket'}]
        buckets = [item['Name'] for item in response['Buckets']]
        self.set_output_property('buckets', buckets)





