"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Keith Robles"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime

from bank_account import *
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.

chequing_account = ChequingAccount(202500, 1, -600,
                                   date(2025, 6, 6), -100, 0.5)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

print(str(chequing_account))
print(chequing_account.get_service_charges())

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

chequing_account.deposit(700)
print(str(chequing_account))
print(chequing_account.get_service_charges())

print("===================================================")

# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.

savings_account = SavingsAccount(202501, 2, 500,
                                 date(2025, 6, 7), 50)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.

print(str(savings_account))
print(savings_account.get_service_charges())

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.

savings_account.withdraw(475)
print(str(savings_account))
print(savings_account.get_service_charges())


print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.

investment_account = InvestmentAccount(202502, 3, 20000,
                                       date(2020, 6, 8), 1.99)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.

print(str(investment_account))
print(investment_account.get_service_charges())

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.

invest_account_2 = InvestmentAccount(202503, 5, 15000,
                                     date(2005, 6, 8), 1.99)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.

print(str(invest_account_2))
print(invest_account_2.get_service_charges())

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.

step_2_charge = chequing_account.get_service_charges()
step_5_charge = savings_account.get_service_charges()
step_8_charge = investment_account.get_service_charges()
step_10_charge = invest_account_2.get_service_charges()

chequing_account.withdraw(step_2_charge)       # Step 2 Account
savings_account.withdraw(step_5_charge)        # Step 5 Account
investment_account.withdraw(step_8_charge)     # Step 8 Account
invest_account_2.withdraw(step_10_charge)      # Step 10 Account

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.

print(str(chequing_account))
print(str(savings_account))
print(str(investment_account))
print(str(invest_account_2))