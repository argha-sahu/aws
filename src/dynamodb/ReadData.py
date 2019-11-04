import boto3
from boto3.dynamodb.conditions import Attr

tableNameToBeCreated = 'Movies'

dynamodb_resource = boto3.resource('dynamodb')
table = dynamodb_resource.Table(tableNameToBeCreated)
print(table)

response = table.get_item(
    Key = {
        'ID' : 1234,
        'Name' : 'Argha Sahu'
    }
)

fe = Attr('SiteId').eq('TDICA07996TRI01')

response = table.scan(
    FilterExpression=fe
)
print(response['Items'])
