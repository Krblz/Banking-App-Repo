"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    
    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        self.Client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")

    def test_init_valid(self):
        # Arrange & Act
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")

        # Assert
        self.assertEqual(1010, client.client_number)
        self.assertEqual("Susan", client.first_name)
        self.assertEqual("Clark", client.last_name)
        self.assertEqual("susanclark@pixell.com", client.email)

    def test_init_invalid_client_number_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            client = Client("A", "Susan", "Clark", "susanclark@pixell.com")

    def test_init_invalid_first_name_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            client = Client(1010, " ", "Clark", "susanclark@pixell.com")

    def test_init_invalid_last_name_raises_exception(self):
        # Arrange & Act
        with self.assertRaises(ValueError):
            client = Client(1010, "Susan", " ", "susanclark@pixell.com")

    def test_init_invalid_email_set_to_default_email(self):
        # Arrange & Act
        client = Client(1010, "Susan", "Clark", "not a email")
        expected = "email@pixell-river.com"

        # Assert
        self.assertEqual(expected, client.email)

    