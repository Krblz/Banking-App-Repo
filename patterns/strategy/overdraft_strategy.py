"""This module defines the Overdraft Strategy class."""

__author__ = "Keith Robles"
__version__ = "Keith Robles"

from bank_account import *
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Overdraft Strategy Class
    Methods:
        calculate_service_charges: Method which extends the
            calculate_service_charges Method of the ServiceChargeStrategy 
            Abstract class
    """
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        __init___: initializes class members to passed parameters.

        args:
            overdraft_limit: The maximum amount a balance can be overdrawn (below 0.00)
                            before overdraft fees are applied.
            overdraft_rate: The rate to which overdraft fees will be applied.
        """
        if isinstance(overdraft_limit, (float, int)):
            self.__overdraft_limit = float(overdraft_limit)
        else:
            self.__overdraft_limit = -100

        if isinstance(overdraft_rate, (float, int)):
            self.__overdraft_rate = float(overdraft_rate)
        else:
            self.__overdraft_rate = 0.05

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        calculate_service_charges method
        returns:
            float
        """
        balance = BankAccount.balance
        
        if (balance >= self.__overdraft_limit):
            service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE
        else:
            service_charge = (ServiceChargeStrategy.BASE_SERVICE_CHARGE +
                            (self.__overdraft_limit - balance)
                             * self.__overdraft_rate)
        return service_charge
    