import boto3

bucket_name = 'argha-testing-bucket'
key = 'pan_card.pdf'
outputName = '/home/argha/pan_card.pdf'

s3_client = boto3.client('s3')
s3_client.download_file(bucket_name, key, outputName)