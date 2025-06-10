""""This Module defines the Investment Account class"""

__author__ = "Keith Robles"
__version__ = "1.0"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """
    Investment Account Class extends from BankAccount
    """

    # Constant for the date 10 years ago
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, account_number: int, client_number: int,
                 balance: float, date_created: date,
                 management_fee: float):
        """
        __init___: initializes class members to passed parameters.

        new args:
            management_fee (float): a float which stores a flat-rate fee the bank charges
                                    for managing an Investment Account        
        """
        super().__init__(account_number, client_number, balance, date_created)

        if isinstance(management_fee, (float, int)):
            self.__management_fee = float(management_fee)
        else:
            self.__management_fee = 2.55

    def __str__(self):
        return (f"{super().__str__()} \n"
                f"Date Created: {self._date_created} "
                f"Management Fee: {self.__management_fee:,.2f} "
                f"Account Type: Investment")

    def get_service_charges(self) -> float:      
        if (self._date_created < self.TEN_YEARS_AGO):
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = (self.BASE_SERVICE_CHARGE +
                            self.__management_fee)
        return service_charge