import boto3

s3_resource = boto3.resource('s3')

BUCKET_NAME = 'argha-copy-testing-bucket'
s3_resource.create_bucket(Bucket=BUCKET_NAME,
                          CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})