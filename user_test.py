import unittest
from user import User

class TestUser(unittest.TestCase):

    """
    test class that defines test cases for the user class behavior

    Args:
    unittest.TestCase: A test class that helps in creating test cases.

    """

    def setUp(self):

        """
        setUp method that runs before every test cases
        """

        self.new_user = User("Jeff", "Master@2025")

    
    def test__init(self):
        """
        To test if the objects are instantiated correctly.
        """

        self.assertEqual(self.new_user.user_name, "Francis")
        self.assertEqual(self.new_user.password, "Master@2025")


    def tearDown(self):

        """
        tearDown method does cleanup after every test has run

        """

        User.users_list=[]

    def test_save_user(self):

        """
        test case to test if users are being saved to users_list
        """

        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)






if __name__ == '__main__':

    unittest.main()
