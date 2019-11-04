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


def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    try:
        username = event['username']
        code = event['code']
        response = client.confirm_sign_up(
            ClientId=CLIENT_ID,
            SecretHash=get_secret_hash(username),
            Username=username,
            ConfirmationCode=code,
            ForceAliasCreation=False, )
    except client.exceptions.UserNotFoundException:
        return event
    except client.exceptions.CodeMismatchException:
        return {"error": True, "success": False, "message": "Invalid Verification code"}
    except client.exceptions.NotAuthorizedException:
        return {"error": True, "success": False, "message": "User is already confirmed"}
    except Exception as e:
        return {"error": True, "success": False, "message": f"Unknown error {e.__str__()} "}

    return event


if __name__ == '__main__':
    event = {
        'username': 'argha.sahu@teradata.com',
        'code': '495232'
    }
    print(lambda_handler(event, None))
