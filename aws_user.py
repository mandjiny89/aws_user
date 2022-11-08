import boto3
iam = boto3.client('iam')

with open('user_list.txt') as f:
    users = f.read()
    users_sorted = users.replace("\n", "")

for user_name in users_sorted.split(","):
    # create a user
    print("pr test using git")
    print("User name added to the IAM ", user_name)
    iam.create_user(UserName=user_name)
    # attach a policy
    iam.attach_user_policy(
    UserName =user_name, 
    PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
    )
