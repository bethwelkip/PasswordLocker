
import secrets


class Credential:
    '''
    Generates new credentials
    '''
    credentials_list = []

    def __init__(self, name, username, password):
        '''
        Defines properties of the credentials

        :param name:
        :param username:
        :param password:
        '''
        self.username = username
        self.password = password
        self.name = name

    def userInput(self, caller):
        if caller == "password":
            opt = input("press y to create password, or press n for me to generate a password for you")
            return opt

    def passworded(self):

        '''
        Allows user to create password or alternatively generates one for the user

        :return:
        '''

        while True:
            opt = self.userInput("password")
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
                return

    @classmethod
    def display_credentials(cls):
        '''
        Loops through the credentials and print their properties: password and username

        :return:
        '''

        if len(Credential.credentials_list) > 0:
            for cred in Credential.credentials_list:
                print(f"\n For {cred.name} your username is: {cred.username}  and your password is: {cred.password}")
        else:
            print("You have no credentials yet")

    @classmethod
    def delete_credential(cls, name):
        '''
        delete the specified credential


        :param name:
        :return:
        '''
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
        '''
        saves the credential object in the class list of instance objects


        :return:
        '''

        Credential.credentials_list.append(self)


if __name__ == '__main__':
    cew = Credential("hu", "hi", "kj")
    print(cew.passworded())





