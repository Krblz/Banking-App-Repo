"""This module defines the Service Change Strategy class."""

__author__ = "Keith Robles"
__version__ = "Keith Robles"

from bank_account import *
from abc import ABC, abstractmethod

class ServiceChangeStrategy(ABC):
    """
    Abstract Class for Payment Strategies.
    Methods:
        calculate_service_charges: Abstract method which will be implemented
            in each of the subclasses of ServiceChargeStrategy based on the specific
            strategy being employed.
    """

    # Constant for Base Service Charge
    BASE_SERVICE_CHARGE = 0.5

    @abstractmethod
    def calculate_service_charges(account: BankAccount) -> float:
        """
        Abstract calculate_service_charges accessor
        returns:
            float
        """
        pass