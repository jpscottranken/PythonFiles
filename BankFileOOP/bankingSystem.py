'''
	Create a Python Banking System Program From Scratch.
	
	There will be the following classes:

	BankAccount				-	The superclass of all other classes.
								      This will be an abstract class.
	
	CheckingAccount   -	Child of BankAccount.
								      All checking accounts must have a
								      minimum balance of $100.00.
	
	SavingsAccount    -	Child of BankAccount
								      All savings accounts must have a.
								      minimum balance of $25.00.

	ChristmasClubAccount	-	Child of BankAccount
								      All Christmas Club accounts must have a
								      minimum balance of $10.00

	Persons should be able to do the following for any type of account:
	
	1.	Check balance.
	2.	Deposit money  into that account.
	3.	Withdraw money from that account.
	4.	Transfer money between accounts.
	5.	Open any type of new Checking, Savings, or Christmas Club account.

	Create objects of each account class (except for BankAccount).
	
	Show examples of checking balance, depositing, and withdrawing
	with each type of account.
	
Explanation:
============
1.	BankAccount (Abstract Class):

Acts as the base class for all types of bank accounts.
Defines abstract methods (checkBalance, deposit, withdraw) that 
must be implemented by subclasses.

Implements a transfer method to transfer funds between accounts.

2.	CheckingAccount:

Inherits from BankAccount.

Enforces a minimum balance of $100.00.

3.	SavingsAccount:

Inherits from BankAccount.

Enforces a minimum balance of $25.00.

4.	ChristmasClubAccount:

Inherits from BankAccount.

Enforces a minimum balance of $10.00.

Examples:
=========
Objects for each child account type are created/instantiated.

Examples will be provided to check balances, deposit,
withdraw, and transfer money between accounts.	
'''

###################################
# https://docs.python.org/3/library/abc.html

from abc import ABC, abstractmethod

####  BankAccount Class  ####
class BankAccount(ABC):
  # Constructor
  def __init__(self, accountHolder, balance):
    self.accountHolder  = accountHolder
    self.balance        = balance

  @abstractmethod
  def checkBalance(self):
    pass

  @abstractmethod
  def deposit(self):
    pass

  @abstractmethod
  def withdraw(self):
    pass

  def transfer(self, amount, targetAccount):
    # Does this much money exist in the account
    if (self.balance >= amount):
      self.withdraw(amount)
      targetAccount.deposit(amount)
      print(f"\nTransferred ${amount:.2f}")# To {targetAccount}")
    else:
      print(f"\nThe Transfer Failed Due To Insufficient Funds.")

###################################

####  CheckingAccount Class  ####
class CheckingAccount(BankAccount):
  MINIMUMBALANCE = 100.00

  def checkBalance(self):
    return (f"The Checking Account Balance For {self.accountHolder} is: ${self.balance:.2f}")

  def deposit(self, amount):
    # Verify that amount to be deposited is positive
    if (amount > 0):
      self.balance += amount
      print(f"Deposited ${amount:.2f} into {self.accountHolder} Checking Account.")
    else:
      print("\nYou Cannot Deposit <= 0")
  
  def withdraw(self, amount):
    tempValue = amount 
    # Verify that amount to be deposited is positive
    if (amount > 0):
      if (self.balance - tempValue < CheckingAccount.MINIMUMBALANCE):
        print(f"\nWithdraw Amount Failed. Would Leave < MINIMUM BALANCE.")
      else:
        self.balance -= amount
        print(f"Withdraw ${amount:.2f} from {self.accountHolder} Checking Account.")
    else:
      print("\nYou Cannot Withdraw <= 0")

###################################

####  SavingsAccount Class  ####

class SavingsAccount(BankAccount):
  MINIMUMBALANCE = 25.00

  def checkBalance(self):
    return (f"The Savings Account Balance For {self.accountHolder} is ${self.balance:.2f}")
  
  def deposit(self, amount):
    # Verify that amount to be deposited is positive
    if (amount > 0):
      self.balance += amount
      print(f"Deposited ${amount:.2f} into {self.accountHolder} Savings Account.")
    else:
      print("\nYou Cannot Deposit <= 0")
  
  def withdraw(self, amount):
    tempValue = amount 
    # Verify that amount to be deposited is positive
    if (amount > 0):
      if (self.balance - tempValue < SavingsAccount.MINIMUMBALANCE):
        print(f"\nWithdraw Amount Failed. Would Leave < MINIMUM BALANCE.")
      else:
        self.balance -= amount
        print(f"Withdraw ${amount:.2f} from {self.accountHolder} Savings Account.")
    else:
      print("\nYou Cannot Withdraw <= 0")

###################################

####  ChristmasClubAccount Class  ####

class ChristmasClubAccount(BankAccount):
  MINIMUMBALANCE = 10.00

  def checkBalance(self):
    return (f"The Christmas Club Account Balance For {self.accountHolder} is ${self.balance:.2f}")
  
  def deposit(self, amount):
    # Verify that amount to be deposited is positive
    if (amount > 0):
      self.balance += amount
      print(f"Deposited ${amount:.2f} into {self.accountHolder} Christmas Club Account.")
    else:
      print("\nYou Cannot Deposit <= 0")
  
  def withdraw(self, amount):
    tempValue = amount 
    # Verify that amount to be deposited is positive
    if (amount > 0):
      if (self.balance - tempValue < ChristmasClubAccount.MINIMUMBALANCE):
        print(f"\nWithdraw Amount Failed. Would Leave < MINIMUM BALANCE.")
      else:
        self.balance -= amount
        print(f"Withdraw ${amount:.2f} from {self.accountHolder} Christmas Club Account.")
    else:
      print("\nYou Cannot Withdraw <= 0")

###################################

def performOperations(inputFile, outputFile):
  with open(inputFile, "r") as infile, \
       open(outputFile, "w") as outfile:
    exec(infile.read(), globals(), locals())

if (__name__ == "__main__"):
  performOperations("input.txt", "output.txt")
