import unittest 
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("qwerty","mmmmmm")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.username,"qwerty")
        self.assertEqual(self.new_user.password,"mmmmmm")
    
    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into the contact list.
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)
    
    def test_save_multiple_user(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact.
        objects to our contact_list
        '''
        self.new_user.save_user() 
        test_user = User("qwerty","mmmmmm") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
if __name__ == '__main__':
    unittest.main()