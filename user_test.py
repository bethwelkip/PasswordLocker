#!/usr/bin/env python3
import builtins
import unittest
from user import User
from credentials import Credential
from unittest.mock import patch

class ContactTest(unittest.TestCase):
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


    def test_create_credential(self):
        '''


        :return:

        '''

        input_one = builtins.input("beth")
        input_two = builtins.input("beth")
        input_three = builtins.input("y")
        input_three = builtins.input("beth")
        user_input = ["beth","beth", "y", "beth"]

    def test_add_credential(self):
        '''


        :return:

        '''
        pass

    def test_create_user(self):
        '''


        :return:

        '''
        pass

    def test_login(self):
        '''


        :return:

        '''
        pass

    def test_save_user(self):
        '''


        :return:

        '''
        pass

    #############################################################################
    ## Test Credentials class                                                  ##
    #############################################################################
    def test_passworded(self):
        '''

        :return:
        '''
        pass
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
        self.assertEqual(len(Credential.credentials_list), 0)  # should fail
        # not working as desired

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
        tests the userInput classes
        :return:
        '''
        # method only incorporates IO dependencies which are not generally tested so no tests here.
        pass

if __name__ == '__main__':
    unittest.main()
