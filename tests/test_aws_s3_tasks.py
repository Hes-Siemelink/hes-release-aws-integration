import unittest

from src.aws_s3_tasks import CreateS3Bucket, ListS3Buckets


class TestS3(unittest.TestCase):

    def test_create_bucket(self):
        # Given
        task = CreateS3Bucket()
        task.input_properties = {
            'server': {
                'url': 'http://digitalai.release.local:4566',
                'username': 'admin',
                'password': 'admin',
                'authenticationMethod': 'Basic'
            },
            'bucketName': 'new-bucket'
        }

        # When
        task.execute_task()

        # Then
        self.assertEqual(task.get_output_properties()['location'], '/new-bucket')

    def test_list_buckets(self):
        # Given
        task = ListS3Buckets()
        task.input_properties = {
            'server': {
                'url': 'http://digitalai.release.local:4566',
                'username': 'admin',
                'password': 'admin',
                'authenticationMethod': 'Basic'
            },
        }

        # When
        task.execute_task()

        # Then
        self.assertEqual(task.get_output_properties()['buckets'], ['/new-bucket'])


if __name__ == '__main__':
    unittest.main()
