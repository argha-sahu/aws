import boto3

from_bucket_name = 'argha-testing-bucket'
file_name = 'pan_card.pdf'
to_bucket_name = 'argha-copy-testing-bucket'
copy_source = {
    'Bucket': from_bucket_name,
    'Key': file_name
}

s3_resource = boto3.resource('s3')
s3_resource.Object(to_bucket_name, file_name).copy(copy_source)