import boto3

dynamodb_resource = boto3.resource('dynamodb')
LearningDynamoDB = dynamodb_resource.Table('Movies')
print(LearningDynamoDB)

response = LearningDynamoDB.put_item(
    Item = {
        'ID' : 1236,
        'Name': 'Soumya Paul',
        'Home' : 'Pune',
        'SiteId' : 'TDICA07996TRI01',
        "CreatedDate": "2019-10-24T10:04:54.445555",
        "Users": [
            {
                "Address1": "NA",
                "City": "NA",
                "ContactNumber": "8888888888",
                "Contacts": [
                    {
                        "contactEmail": "NA",
                        "contactName": "NA"
                    }
                ],
                "Country": "US",
                "CountryCode": "1",
                "Email": "testing@vt01.com",
                "FirstName": "Testing",
                "LastName": "Testing",
                "State": "NA",
                "ZipCode": "3333"
            },
            {
                "Address1": "NA",
                "City": "NA",
                "ContactNumber": "8888888888",
                "Contacts": [
                    {
                        "contactEmail": "NA",
                        "contactName": "NA"
                    }
                ],
                "Country": "US",
                "CountryCode": "1",
                "Email": "lynn.Nichols@vt01.com",
                "FirstName": "Lynn",
                "LastName": "Nichols",
                "State": "NA",
                "ZipCode": "3333"
            }],
        'Education' : {
            'B.Tech' : 'University Of Calcutta',
            'M.Tech' : 'University Of Hyderabad'
        }
    }
)
