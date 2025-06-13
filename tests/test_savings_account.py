"""
Description: Unit tests for the InvestmentAccount class.
Author: Keith Robles
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py
"""

import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestClient(unittest.TestCase):

    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        self.investment_account  = SavingsAccount(20025, 1, 0,
                                                     date(2012, 6, 6), 2.00)
        self.BASE_SERVICE_CHARGE = self.investment_account.BASE_SERVICE_CHARGE
        
    def test_init_valid(self):
        # Arrange & Act
        investment_account  = InvestmentAccount(20025, 1, 0,
                                                date(2025, 6, 6), 2.00)
        management_fee = investment_account._InvestmentAccount__management_fee

        # Assert
        self.assertEqual(2.00, management_fee)
