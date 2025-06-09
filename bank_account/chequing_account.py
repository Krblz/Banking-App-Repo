""""This Module defines the Chequing Account class"""

__author__ = "Keith Robles"
__version__ = "1.0"

from datetime import date
from bank_account.bank_account import BankAccount
from abc import ABC, abstractmethod

class ChequingAccount(BankAccount):
    """
    Chequing Account Class extends from BankAccount
    """
    def __init__(self, account_number: int, client_number: int, 
                 balance: float, date_created: date, overdraft_limit: float,
                 overdraft_rate: float):
        """
        __init___: initializes class members to passed parameters.

        new args:
            overdraft_limit: The maximum amount a balance can be overdrawn (below 0.00)
                            before overdraft fees are applied.
            overdraft_rate: The rate to which overdraft fees will be applied.
        
        """
        super().__init__(account_number, client_number, balance, date_created)

        if isinstance(overdraft_limit, (float, int)):
            self.__overdraft_limit = float(overdraft_limit)
        else:
            self.__overdraft_limit = -100

        if isinstance(overdraft_rate, (float, int)):
            self.__overdraft_rate = float(overdraft_rate)
        else:
            self.__overdraft_rate = 0.05

    def __str__(self):
        return (f"{super().__str__()} \n"
                f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                f"Overdraft Rate: {self.__overdraft_rate}% "
                f"Account Type: Chequing")

    def get_service_charges(self) -> float:
        if (self.__balance >= self.__overdraft_limit):
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = (self.BASE_SERVICE_CHARGE +
                            (self.__overdraft_limit - self.__balance)
                             * self.__overdraft_rate)
        return service_charge

