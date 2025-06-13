""""This Module defines the Savings Account class"""

__author__ = "Keith Robles"
__version__ = "1.0"

from datetime import date
from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """
    Savings Account Class extends from BankAccount
    """
    
    # Constant for Premium Charge
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date,
                 minimum_balance: float):
        """
        __init___: initializes class members to passed parameters.

        new args:
            minimum_balance (float): a float which stores a minimum value a balance
                                    can be before further service charges are applied
        """
        super().__init__(account_number, client_number, balance, date_created)

        if isinstance(minimum_balance, (float, int)):
            self.__minimum_balance = float(minimum_balance)
        else:
            self.__minimum_balance = 50.00

    def __str__(self) -> str:
        return (f"{super().__str__()} \n"
                f"Minimum Balance: ${self.__minimum_balance:,.2f} "
                f"Account Type: Savings")

    def get_service_charges(self) -> float:
        if (self._BankAccount__balance >= self.__minimum_balance):
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = (self.BASE_SERVICE_CHARGE *
                            self.SERVICE_CHARGE_PREMIUM)
        return service_charge