#!/usr/bin/env python3
# import secrets as sc
from credentials import Credential


class User:
    users = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, name):
        if User.users:
            for user in User.users:
                if user.username == name:
                    attempt = 0
                    while attempt < 3:
                        password = input("please input the password of your account")
                        if user.password == password:
                            print("You are now logged in")
                            return user
                        else:
                            print("wrong password :(")
                        attempt += 1
                    print("You have run out of password attempts")
                    return None
            print("No such a user exists")
            return None

        else:
            print("No users currently saved in the system")





    # def password(self):
    #     pass

    def find_account(self):
        pass

    def username(self):
        pass

    def save_user(self):
        User.users.append(self)

    @classmethod
    def create_user(cls, username, password):
        user = User(username, password)
        user.save_user()

    def add_credential(self):
        print("Please provide me with the name of the credential you would like to add  eg Twitter, Instagram \n")
        name = input()
        username = input("please provide your username as on the credential")
        password = input("please provide your password on the credential \n")
        new_cred = Credential(name, username, password )
        new_cred.save_credential()
        print("Length of list:  ", len(Credential.credentials_list))

    def create_credential(self):
        pass

    def display_creds(self):
        Credential.display_credentials()

    def delete_credential(self):
        name = input("name of credential to be deleted? \n")
        Credential.delete_credential(name)
        print("Length of list:  ", len(Credential.credentials_list))


if __name__ == '__main__':
    new = User("hi", "me")
    new.add_credential()
    new.delete_credential()
    new.display_creds()

    #
    # print(sc.token_urlsafe(16))
    # while True:
    #     print("type the following shortcode to choose the action you'd like to do: \n cc:   create user account \n "
    #           "lc:  log into existing user account \n ad:    add credential \n dd:   delete credential \n dc:  display "
    #           "credentials "
    #           "\n  ")
    #     opt = input("shortcode: ")
    #     if opt == "cc":
    #         print("please provide a username for your account")
    #         username = input()
    #         password = input("please the password you'd like for your account")
    #         User.create_user(username, password)
    #     elif opt == "lc":
    #         pass
    #     elif opt == "ad":
    #         pass
    #     elif opt == "dd":
    #         pass
    #     elif opt == "dc":

