"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

from client.client import Client

class TestClient(unittest.TestCase):
    
    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        self.Client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")

    def test_init_valid(self):
        # Arrang & Act
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")

        # Assert
        self.assertEqual(1010, client.__client_number)
        self.assertEqual("Susan", client.__first_name)
        self.assertEqual("Clark", client.__last_name)
        self.assertEqual("susanclark@pixell.com", client.__email_address)

    