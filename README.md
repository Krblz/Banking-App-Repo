# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Keith Robles

## Assignment
Assignment 1: Classes, Encapsulation and Unit Test Planning  
Assignment 2: Abstraction, Inheritance, and Polymorphism  
Assignment 3: Design Patterns  

## Encapsulation
Encapsulation is achieved in BankAccount Class by inputting values into an instance
of the BankAccount Class. The BankAccount Class also correctly checks for Errors and 
messages appropriate statements regarding the Errors.  
BankAccount Class also has methods like Withdraw, Deposit, and Balance that provides
access to the values from inside the Instance.

## Polymorphism
Polymorphism is achieved in ChequingAccount, InvestmentAccount, and SavingsAccount by  
using the BankAccount Class as their Superclass. This allows them to inherit the attributes  
and methods of the Superclass. As a Subclass, they also override the method get_service_charges  
with their own respective changes. Dynamic Binding is observed working through the Tests and  
the AO2_Main where each account made from the Subclasses used the Deposit and Withdraw Method  
from BankAccount Superclass. Each instance is the method invoked depends on the runtime of each  
respective instances created during the program's runtime. 