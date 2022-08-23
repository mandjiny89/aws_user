import boto3
iam = boto3.client('iam')

with open('user_list.txt') as f:
    users = f.read()
    users_sorted = users.replace("\n", "")

for user_check in iam.list_users()['Users']:
    exist_already = ("{0}".format(user_check['UserName']))
    # print(exist_already)
    for user_name in users_sorted.split(","):
        if user_name != exist_already:
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