#!/usr/bin/env python3

import unittest
from user import User
from credentials import Credential

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

    def tearDown(self):
        '''


        :return:
        '''
        pass

    def test_init(self):
        '''


         :return:
        '''
        pass

    def test_save_credentials(self):
        '''


        :return:
        '''
        pass

    def test_display_creds(self):
        '''


        :return:

        '''
        pass

    def test_delete_credential(self):
        '''


        :return:

        '''
        pass

    def test_create_credential(self):
        '''


        :return:

        '''
        pass

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
    def test_password(self):
        '''

        :return:
        '''
        pass
    def test_display_credentials(self):
        '''


        :return:
        '''
        pass

    def test_delete_credential(self):
        '''

        :return:
        '''
        pass

    def test_save_credential(self):
        '''

        :return:
        '''
        pass


if __name__ == '__main__':
    unittest.main()
