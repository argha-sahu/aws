import boto3

s3 = boto3.client('s3')
bucket_name = 'argha-testing-bucket'
file_name = '/home/argha/pan caard.pdf'
key_name = 'pan_card.pdf'
s3.upload_file(file_name, bucket_name, key_name)