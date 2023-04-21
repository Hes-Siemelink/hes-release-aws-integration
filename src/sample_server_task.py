from digitalai.release.integration import BaseTask

import boto3


class ServerQuery(BaseTask):
    """
        Fetches product details from a remote server
    """

    def execute(self) -> None:

        # Build request from input
        server = self.input_properties['server']
        if server is None:
            raise ValueError("Server field cannot be empty")
        server_url = server['url'].strip("/")
        auth = (server['username'], server['password'])
        product_id = self.input_properties['productId']
        request_url = f"{server_url}/products/{product_id}"

        # Make request
        endpoint_url = "http://digitalai.release.local:4566"
        client = boto3.client("lambda", endpoint_url=endpoint_url, region_name='eu-west-2',
                              aws_access_key_id="", aws_secret_access_key="")
        result = client.list_functions()

        print(result)





