

class Credential:
    credentials_list  = []
    def __init__(self):
        self.username = self.username()
        self.password = self.password()

    def password(self):
        while True:
            print("press y to create password, or press n for me to generate a password for you")
            opt = input()
            if opt == "y":
                print("please input your preferred password")
                password = input()
                return password
            elif opt == "n":
                return f"hdhsj{opt}ihsyrwgka"
            else:
                print("You did not make the right choice")
    def username(self):
        print("please enter your credential user name")
        user = input()
        return user

    def display_credentials(self):
        for cred in Credential.credentials_list:
            print("/n")
            print(f"For {cred} your username is: {cred.username} and your password is: {cred.password}")

    def delete_credential(self):
        pass
    def save_credential(self):
        pass


if __name__ == '__main__':
    print("hi")

