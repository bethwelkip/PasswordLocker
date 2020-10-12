#!/usr/bin/env python3
# import secrets as sc
from credentials import Credential


class User:
    users = []

    def __init__(self, username, password):
        '''
        Initializes the user class with a username and password
        :param username:
        :param password:
        '''
        self.username = username
        self.password = password

    @classmethod
    def login(cls):
        '''
        Method logs a user in if they provide the correct username and password combination
        Args:
            class
        :return:
        '''
        name = input("provide the username of your account")
        if User.users:
            for user in User.users:
                if user.username == name:
                    attempt = 0
                    while attempt < 3:
                        attempts = 2-attempt
                        password = input(f"please input the password of your account. You have {attempts} attempts "
                                         f"left")
                        if user.password == password:
                            print("You are now logged in")
                            return user
                        else:
                            print("wrong password :(")
                        attempt += 1
                    print("You have run out of password attempts.")
                    return
            print("No such a user exists")
            return None

        else:
            print("No users currently saved in the system")

    def save_user(self):
        '''
        saves the user object into a list available to entire class.
        :return:
        '''
        User.users.append(self)

    @classmethod
    def create_user(cls):
        '''
        Creates a user account once provided with username and password
        Args:
            class
        :return:
        '''
        print("please provide a username for your account")
        username = input()
        password = input("please the password you'd like for your account\n")
        user = User(username, password)
        user.save_user()
        return user

    def add_credential(self):
        '''

        :return:
        '''

        print("Please provide me with the name of the credential you would like to add  eg Twitter, Instagram \n")
        name = input()
        username = input("please provide your username as on the credential\n")
        password = input("please provide your password on the credential \n")
        new_cred = Credential(name, username, password )
        new_cred.save_credential()
        print("Length of list:  ", len(Credential.credentials_list))

    def create_credential(self):
        '''


        :return:
        '''
        # print("Please provide me with the name of the credential you would like to create  eg Twitter, Instagram \n")
        name = self.userInput("create_cred_name") # input()
        username = self.userInput("create_cred_user") # input("please provide the username you would like to have on the
        # credential
        # \n")
        password = Credential.passworded(Credential("", "", "'"))
        new_cred = Credential(name, username, password)
        new_cred.save_credential()

        print("Length of list:  ", len(Credential.credentials_list))

    def display_creds(self):
        '''


        :return:
        '''
        Credential.display_credentials()

    def delete_credential(self):
        '''


        :return:
        '''
        name = self.userInput("delete") # input("name of credential to be deleted? \n")
        Credential.delete_credential(name)
        print("Length of list:  ", len(Credential.credentials_list))
        pass
    def userInput(self, caller):
        if caller == "delete":
            name = input("name of credential to be deleted? \n")
            return name

        elif caller == "create_cred_user":
            name = input("please provide the username you would like to have on the credential \n")
            return name
        elif caller == "create_cred_name":
            option = input("Please provide me with the name of the credential you would like to create  eg Twitter, "
                         "Instagram \n")
            return option
        elif caller == "add":
            pass
        elif caller == "create_user":
            pass
        elif caller == "login_user":
            pass
        else:
            pass



if __name__ == '__main__':

    print("Welcome to Password Locker")
    state = True
    # new_user = ""
    while state:
        print("type the following shortcode to choose the action you'd like to do: \n cc:   create user account \n "
                  "lc:  log into existing user account \n ctc:  create credential \n ad:    add credential \n "
              "dd:   delete credential \n dc:  "
              "display "
                  "credentials "
              " \n  x:    exit application")
        opt = input("shortcode: ")
        if opt == "cc":
            new_user = User.create_user()
        elif opt == "lc":
            possUser = User.login()
            if possUser:
                new_user = possUser
            else:
                print("Sorry you were not able to log in. Try again later:( \n")

        elif opt == "ad":
            if len(User.users) > 0:
                new_user.add_credential()
            else:
                print("No user to delete his/her/their credentials \n")

        elif opt == "dd":
            if len(User.users) > 0:
                new_user.delete_credential()
            else:
                print("No user to delete his/her/their credentials \n")

        elif opt == "ctc":
            if len(User.users) > 0:
                new_user.create_credential()
            else:
                print("No user to create his/her/their credentials \n")
        elif opt == "dc":
            if len(User.users)> 0:
                new_user.display_creds()
            else:
                print("No user to show his/her/their credentials")
        elif opt == "x":
            print("Thank you for checking us out. Good Bye and Goodluck")
            state = False
        else:
            print("invalid code. Please try again")



