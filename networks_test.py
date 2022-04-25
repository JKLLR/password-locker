import unittest
from networks import Credentials

class TestCredentials(unittest.TestCase):

    """
    test class that defines test cases for credentials classes

    Args:
    unittest.TestCase: helps in creating test cases

    """

    def setUp(self):
        """
        setuP method that runs before each test case
        """
        self.new_network = Credentials("Twitter", "JeffHuria", "Qwerty@2025")

    def tearDown(self):
        """
        method to clear fields after unit tests are run
        """
        Credentials.network_list=[]

    
    def test_init(self):


        """
        test whether the objects are initialized correctly

        """
        self.assertEqual(self.new_network.network_name, "Twitter")
        self.assertEqual(self.new_network.network_username, "JeffHuria")
        self.assertEqual(self.new_network.network_password, "Qwerty@2025")
    

    def test_save_credentials(self):

        self.new_network.save_credentials()
        self.assertEqual(len(Credentials.network_list), 1)

    
    def test_save_multiple_networks(self):

        """
         Test to see if we can save more than one object in our network_list\

        """
        self.new_network.save_credentials()
        test_account = Credentials("Google", "BaconLover", "Happy2help")
        test_account.save_credentials()

        self.assertEqual(len(Credentials.network_list), 2)
     
    def test_display_credentials(self):
        """ 
        Test for the method that returns all the credentials stored

        """
        self.assertEqual(Credentials.display_credentials(), Credentials.network_list)



    def test_delete_credentials(self):
        """
        test to delete a credential
        """
        self.new_network.save_credentials()
        test_account = Credentials("Google", "BaconLover", "Happy2help")
        test_account.save_credentials()
        
        self.new_network.delete_credentials()
        self.assertEqual(len(Credentials.network_list), 1)
    
    def test_credential_exists(self):
        self.new_network.save_credentials()
        test_account = Credentials("Google", "BaconLover", "Happy2help")
        test_account.save_credentials()

        credential_exists = Credentials.credential_exists("Google")
        self.assertTrue(credential_exists)

    
    def test_search_credentials(self):
        self.new_network.save_credentials()
        test_account = Credentials("Google", "BaconLover", "Happy2help")
        test_account.save_credentials()

        search_credentials = Credentials.search_credentials("Google")
        self.assertEqual(search_credentials.network_username, "BaconLover")

        




if __name__=='__main__':
    unittest.main()