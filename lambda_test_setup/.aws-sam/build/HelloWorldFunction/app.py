import json
import boto3
# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    userAdd = UserAdd()
    userAdd.userCreation()
    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "hello world, testing new change",
            # "location": ip.text.replace("\n", "")
        }),
        "headers": {
            "Content-Type": "application/json",
        }
    }

class UserAdd:
    def __init__(self):
        print("############  Class Started  ##############")

    def userCreation(self):
        print("printing with open")
        with open('user_list.txt') as f:
            users = f.read()
            users_sorted = users.replace("\n", "")

        existing_user = []
        iam = boto3.client('iam')
        for user_check in iam.list_users()['Users']:
            existing_user_list = ("{0}".format(user_check['UserName']))
            existing_user += existing_user_list.split(",")
        print("List of users already exisit", existing_user)

        for user_name in users_sorted.split(","):
            if user_name not in existing_user:
                # create a user
                print("Printing the user name added to the IAM ", user_name)
                iam.create_user(UserName=user_name)
                # attach a policy
                iam.attach_user_policy(
                UserName =user_name, 
                PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
                )
            else:
                print("User already exit", user_name)

