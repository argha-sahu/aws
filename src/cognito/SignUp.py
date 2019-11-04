import boto3
import hmac
import hashlib
import base64

USER_POOL_ID = 'us-east-2_xMNNdq3IN'
CLIENT_ID = '6enfchdko4o74cse26b689m6nq'
CLIENT_SECRET = '1r0mg0jfppihnqa4ddju7qvoigskd1ule9795v2v83p92l6fpram'


def get_secret_hash(username):
    msg = username + CLIENT_ID
    dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'),
                   msg=str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2


ERROR = 0
SUCCESS = 1
USER_EXISTS = 2


def sign_up(username, password, name, email):
    client = boto3.client('cognito-idp')
    try:
        resp = client.sign_up(
            ClientId=CLIENT_ID,
            SecretHash=get_secret_hash(username),
            Username=username,
            Password=password,
            UserAttributes=[
                {
                    'Name': "name",
                    'Value': name
                },
                {
                    'Name': "email",
                    'Value': email
                }
            ],
            ValidationData=[
                {
                    'Name': "email",
                    'Value': email
                },
                {
                    'Name': "custom:username",
                    'Value': username
                }],

        )

    except client.exceptions.UsernameExistsException as e:
        return USER_EXISTS, e.__str__()
    except client.exceptions.InvalidPasswordException as e:
        return ERROR, "Password should have Caps, Special chars, Numbers"
    except client.exceptions.UserLambdaValidationException as e:
        return ERROR, "Email already exists"
    except Exception as e:
        return ERROR, e.__str__()
    return SUCCESS, None


def lambda_handler(event, context):
    for field in ["username", "email", "password", "name"]:
        if not event.get(field):
            return {"error": False, "success": True, 'message': f"{field} is not present", "data": None}
    username = event['username']
    email = event["email"]
    password = event['password']
    name = event["name"]
    signed_up, msg = sign_up(username, password, name, email)

    if msg != None:
        return {'message': msg, "error": True, "success": False, "data": None}
    return {"error": False, "success": True, 'message': "Please confirm your signup, check Email for validation code",
            "data": None}


if __name__ == '__main__':
    event = {
        'username': 'venkataphanikumar.jogi@teradata.com',
        'email': 'venkataphanikumar.jogi@teradata.com',
        'password': 'password_phani',
        'name': 'Phani Jogi'
    }
    print(lambda_handler(event, None))
