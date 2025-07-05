"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Keith Robles"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

from bank_account import *
from datetime import date
from client.client import Client

# 2. Create a Client object with data of your choice.

client_1 = Client(1, "Rice", "Shower", "rshowerbluerose@uma.com")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.

chequing_1 = ChequingAccount(20200, 1, 1000, date(2025, 7, 4), -100, 0.5)
savings_1 = SavingsAccount(20200, 1, 1500, date(2025, 4, 4), 50)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).

chequing_1.attach(client_1)
savings_1.attach(client_1)

# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.

client_2 = Client(2, "Haru", "Urara", "harurara_113@uma.com")
savings_2 = SavingsAccount(19960, 2, 113, date(2004, 8, 4), 50)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

try:
    # Step 3 Rice Shower Account
    savings_1.withdraw(600) # Deposits Normal
    chequing_1.withdraw(996) # Withdraws to lower balance
    savings_1.deposit(10400) # Deposit Larger than Threshold 
    
    # Step 5 Haru Urara Account
    savings_2.deposit(10900) # Deposits Larger than Threshold
    savings_2.withdraw(10000) # Withdraws Normally
    savings_2.withdraw(12) # Withdraws to lower balance

except ValueError as e:
    print(e)