#!/usr/bin/env python3
import builtins
import unittest
from user import User
from credentials import Credential
from unittest.mock import patch

class userTest(unittest.TestCase):
    '''
       defines test cases for the user class behaviors
       Args:
           unittest.TestCase: TestCase class that helps in creating test cases

     '''

    def setUp(self):
        '''


        :return:
        '''
        self.user_one = User("Bethu", "Kip")
        self.cred_one = Credential("twitter", "bethu", 'kip')

    def tearDown(self):
        '''


        :return:
        '''
        Credential.credentials_list = []
        User.users = []

    def test_init(self):
        '''


         :return:
        '''
        self.assertEqual(self.user_one.password, "Kip")
        self.assertEqual(self.user_one.username, "Bethu")
        self.assertEqual(self.cred_one.name, "twitter")
        self.assertEqual(self.cred_one.password, "kip")
        self.assertEqual(self.cred_one.username, "bethu")


    def test_login(self):
        '''

        tests the login method of the user class. users 'patch' and  'builtins' to simulate user input
        :return:

        '''
        User.users.append(self.user_one)
        user_input = ["Bethu","Kip"]
        with patch('builtins.input', side_effect = user_input):
            new_user = User.login()
        print(new_user.password)
        self.assertEqual(self.user_one,new_user ) #passed!!!!!
    def test_add_credential(self):
        '''


        :return:

        '''
        user_input = ["twittr", "bethu", "kip"]
        with patch('builtins.input', side_effect=user_input):
            self.user_one.add_credential()
        self.assertEqual(len(Credential.credentials_list), 1)  # creating a new credential saves into my list of
        # credentials
        self.assertEqual(Credential.credentials_list[0].name, "twittr" )

    def test_create_user(self):
        '''


        :return:

        '''
        user_input = ["bethu", "kip"]
        with patch('builtins.input', side_effect=user_input):
            User.create_user()
        self.assertEqual(len(User.users), 1)  # creating a new user saves into my list of
        # users

    def test_create_credential(self):
        '''
        tests the create_credential method of User class.

        :return:

        '''
        self.user_one.save_user()
        Credential.credentials_list.append(self.cred_one)
        user_input = ["twittr", "bethu", "y", "kip"]
        with patch('builtins.input', side_effect=user_input):
            self.user_one.create_credential()
        self.assertEqual(len(Credential.credentials_list), 2) #creating a new credential saves into my list of
        # credentials


    def test_save_user(self):
        '''

        tests the User method 'save_user'
        :return:

        '''
        self.user_one.save_user()
        User.users.append(self.user_one)
        self.assertEqual(len(self.user_one.users), 2)
    def test_display_creds(self):
        '''
        tests the user method 'display_creds'
        :return:
        '''
        Credential.credentials_list.append(self.cred_one)
        self.assertEqual(self.user_one.display_creds(), Credential.display_credentials())

    #############################################################################
    ## Test Credentials class                                                  ##
    #############################################################################
    def test_passworded(self):

        '''

        :return:
        '''

        user_input = ["y", "new"]
        with patch('builtins.input', side_effect=user_input):
            passw = self.cred_one.passworded()
        self.assertEqual(passw, "new")

        # Note: hard to test the randomly generated response because the result is always different
        # Here's  my attempt at it: confirm that the two generated passwords are not equal

        ran_in = "n"
        with patch('builtins.input', side_effect=ran_in):
            passw1 = self.cred_one.passworded()
        ran_in1 = "n"
        with patch('builtins.input', side_effect=ran_in1):
            passw2 = self.cred_one.passworded()
        self.assertNotEqual(passw1, passw2)

    def test_display_credentials(self):
        '''


        :return:

        '''
        printed = f"\n For {self.cred_one.name} your username is: { self.cred_one.username}  and your password is: {self.cred_one.password}"
        Credential.credentials_list.append(self.cred_one)
        self.assertEqual(Credential.display_credentials(), builtins.print(printed))

    def test_delete_credential(self):
        '''

        :return:
        '''
        Credential.credentials_list.append(self.cred_one)
        Credential.delete_credential(self.cred_one.name)
        self.assertEqual(len(Credential.credentials_list), 0)  # list is now empty

    def test_save_credential(self):

        '''


        :return:
        '''
        Credential.credentials_list.append(self.cred_one)
        User.users.append(self.user_one)
        self.assertEqual(len(Credential.credentials_list), 1)
        self.assertEqual(len(User.users), 1)
    def test_userInput(self):
        '''
        tests the userInput methods of Credential and User classes
        :return:
        '''
        # method only incorporates IO dependencies which are not generally tested so only 1 tests here.
        ran_in = ["y", "password", "n"]
        with patch('builtins.input', side_effect=ran_in):
            passw1 = self.cred_one.userInput(ran_in[1])
        self.assertEqual(passw1, "y")
if __name__ == '__main__':
    unittest.main()
