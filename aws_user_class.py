import boto3
iam = boto3.client('iam')
class UserAdd:
    def __init__(self):
        print("############  Class Started  ##############")

    def userCreation(self):
        print("printing with open")
        with open('user_list.txt') as f:
            users = f.read()
            users_sorted = users.replace("\n", "")

        existing_user = []
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

if __name__ == '__main__':
    userAdd = UserAdd()
    userAdd.userCreation()