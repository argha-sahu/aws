import boto3

bucket_name = 'argha-copy-testing-bucket'
file_name = 'pan_card.pdf'

s3_resource = boto3.resource('s3')
s3_resource.Object(bucket_name, file_name).delete()