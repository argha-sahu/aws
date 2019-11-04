import boto3

dynamodb_client = boto3.client('dynamodb')
tables = dynamodb_client.list_tables()['TableNames']
print(tables)

tableNameToBeCreated = 'Movies'

if tableNameToBeCreated not in tables:
    response = dynamodb_client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'ID',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'Name',
                'AttributeType': 'S'
            }
        ],
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName': 'ID',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'Name',
                'KeyType': 'RANGE'
            }
        ],
        BillingMode='PROVISIONED',
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        },
        Tags=[
            {
                'Key': 'Creator',
                'Value': 'Argha Sahu'
            },
        ]
    )