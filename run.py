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

def delete_network_credentials(network):
    """
    Function to delete a network's credentials"""
    network.delete_credentials()

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
