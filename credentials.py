
import secrets


class Credential:
    credentials_list  = []

    def __init__(self, name, username, password):
        self.username = username
        self.password = password
        self.name = name

    def password(self):
        while True:
            print("press y to create password, or press n for me to generate a password for you")
            opt = input()
            if opt == "y":
                print("please input your preferred password")
                password = input()
                return password
            elif opt == "n":
                passw = secrets.token_urlsafe()
                print("Your system generated password is:  ", passw)
                # lenn = int(input("what's the length of the password you want me to generate? eg  "))
                # return passw[:lenn]
                return passw
            else:
                print("You did not make an acceptable choice")

    def username(self):
        print("please enter your credential user name")
        user = input()
        return user

    @classmethod
    def display_credentials(self):
        if Credential.credentials_list:
            for cred in Credential.credentials_list:
                print("/n")
                print(f"For {cred.name} your username is: {cred.username}")  # and your password is: {cred.password}
        else:
            "You have no credentials yet"

    @classmethod
    def delete_credential(self, name):
        if Credential.credentials_list:
            for cred in Credential.credentials_list:
                if cred.name == name:
                    Credential.credentials_list.remove(cred)
                    print(f"The credential {cred.name} has been deleted")
                    return
            print("No such a credential exists")
        else:
            print("No credentials saved yet. Please save before deleting")

    def save_credential(self):
        Credential.credentials_list.append(self)


if __name__ == '__main__':
    print("hi")

