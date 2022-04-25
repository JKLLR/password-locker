class Credentials:

    """
    class that creates new instances of network credentials
    """

    network_list=[]

    def __init__(self, network_name, network_username, network_password):

        """


        """
        self.network_name=network_name
        self.network_username=network_username
        self.network_password=network_password


    def save_credentials(self):

        """
        method to save credentials to the network_list
        """
        Credentials.network_list.append(self)

    @classmethod
    def credential_exists(cls, network_name):

        """
        Args: network_name
        Returns a boolean if credential exists
        """
        for network in cls.network_list:
            if network.network_name == network_name:
                return True
        return False


    @classmethod
    def search_credentials(cls, network_name):

        """
        Args:network_name
        """

        for network in cls.network_list:
            if network.network_name == network_name:
                return network
            
        
        return "The network does not exist"




    @classmethod
    def display_credentials(cls):
        """
        Method to display all objects in the contact list
        """

        return cls.network_list
        
        
        
    def delete_credentials(self):

        """
        Method to delete a credential from network_list
        """

        Credentials.network_list.remove(self)