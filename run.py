#!/usr/bin env python3

from user import User
from networks import Credentials
import random 
import string

def create_user(user_name, password):

    """
    Function for creating a new User
    """

    new_user = User(user_name, password)
    return new_user

def save_new_user(user):

    """
    Function to save user to user list
    """
    user.save_user()

def create_new_network(network_name, network_username, network_password):

    """
    Function to create new network credentials
    """

    new_network= Credentials(network_name, network_username, network_password)
    return new_network

def save_network_credentials(network):

    """
    function to save a new network's credentials
    """
    network.save_credentials()

def delete_network_credentials(network_name):
    """
    Function to delete a network's credentials
    """
    network = Credentials.search_credentials(network_name)
    return network.delete_credentials()


def display_networks():

    """
    function to show all credentials saved
    """
    return Credentials.display_credentials()

def create_password(length=10):

    """
    Function for generating a password
    """
    characters = string.ascii_letters +string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))


def search_network_credentials(network_name):

    username = Credentials.search_credentials(network_name).network_username
    password = Credentials.search_credentials(network_name).network_password
    return  print(f"Network Username:{username}, Network Password {password}")







def main():
    print("Hello there. Welcome to Password Locker. Your secrets keeper. What is your name?")
    print("\n")
    user_name=input()
    print("\n")
    print(f'Hello {user_name}!')
    print("You can use these short codes to navigate through Password_Locker")
    print("\n")
    while True:
        print('cc-Create a password locker account')
        print('lg- Login to you password_Locker account')
        print('ex- Exit your password locker account')
        print('\n')

        short_code = input().lower()

        if short_code =='cc':
            print('Create your password Locker account')
            print("_"*10)
            print("First, enter your username")

            user_name = input()
            print(f'{user_name}. Enter a Password')
            password=input()


            save_new_user(create_user(user_name, password))

            print("\n")

            print(f'Hurray!, {user_name}, your account has successfully been created')

            print("\n")

            print('Try login in to your password locker account')

            print('Enter your username')
            login_username=input()

            print('Enter the password you just created')
            login_password=input()
            

            if user_name!=login_username or password != login_password:
                print('Invalid user_name or password!')
                print('Please login in again try again')

                login_username=input()

                login_password=input()

            else:
                print('\n')
                print(f'Welcome to your password locker account {user_name}')
                add_networks()

                print('\n')
                save_new_user(login_username, login_password)
                
        elif short_code =='lg':
                print("Log in to your existing account")
                print("Enter your username")
                lg_username=input()
                print("Enter your password")
                lg_password = input()

                if lg_username !='Francis' and lg_password !='Master@2025':
                    print("Please create a password locker account")

                else:
                    print(f'Hello {lg_username}. Welcome to you personal secrets keeper')
                    print('\n')
                    add_networks()
                    
                
        elif short_code == 'ex':
            print("Welcome back any time. Cheers!")
            break
        else:
            print("Invalid short code. Try again")

            
            print('\n')

    
def add_networks():
        print ("With you account ready, you can now save credentials of any network in here ")
        print("These are the short codes for navigating through")
        print('\n')

        while True:
            print('\n')
            print("**"*15)

            print('ann-Add new credentials for any of your networks')

            print('aen - Add an existing credentials for your networks')
            print('view- Get to see all the credentials you have saved')
            print('del- Delete saved network credentials')
            print('sc - search for a network by network_name')
            print('exit- Exit from your account')
            print("**"*15)


            short_code = input().lower()



            if short_code =='ann':
                print ('Add credentials for a new network')
                print('_'*10)

                print('Network_Name:')
                network_name=input()

                print('Network_Username')
                network_username=input()


                print('\n')
                print('For you password, enter either of the shortcodes')
                print('gp- Let Password_Locker generate a password for your network')
                print('mp- Enter my own password')

                short_code = input().lower()


                if short_code =='gp':

                    network_password= create_password()
                    print(network_password)
                elif short_code=='mp':
                    print("Network Password")
                    network_password = input()
                
                else:
                    print("Invalid short code")
                

                save_network_credentials(create_new_network(network_name, network_username, network_password))

                print(f'Credentials for {network_name} have been added to your network list')
            

            elif short_code=='aen':
                print('Add existing network credentials')
                print('_'*15)
                print('Network_Name')
                network_name=input()
                
                print('Network_Username')
                network_username=input()

                print("Network_Password")
                network_password=input()

                save_network_credentials(create_new_network(network_name, network_username, network_password))

                print(f'Credentials for {network_name} have been successfully saved')
            
            elif short_code == 'sc':

                print("Enter the name of the network")
                network_name= input()
                print(network_name)
                search_network_credentials(network_name)


            elif short_code == 'view':
                if display_networks():
                    print('Here is a list of all your saved network credentials')
                    print("__"*30)

                    for network in display_networks():
                        print(f'{network.network_name}, {network.network_username}, {network.network_password}')


                    print('\n')
                else:
                    print('\n')
                    print('No network credentials found')


            elif short_code =='del':

                print("Enter network_name to delete")
                network_name= input()
                delete_network_credentials(network_name)
                print(f"Credentials for {network_name} have been deleted")
            

            elif short_code == 'exit':
                print('Thank you for visiting Password_ Locker.')
                print('Have a good one')
                break

if __name__=='__main__':
 main()