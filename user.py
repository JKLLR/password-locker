class User:

    """
    A class that creates new instances of users
    """

    users_list =[]

    """
    A variable to store new instances of users in a list

    """

    def __init__(self, user_name, password):

      """
       __init__ method helps us define properties for our objects

       Args:
       user_name:Name of PasswordLocker user
       password: Password to PasswordLocker for said user

       """

      self.user_name = user_name
      self.password = password


    
    def save_user(self):

        User.users_list.append(self)