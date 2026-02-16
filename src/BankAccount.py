#!/usr/bin/env python3
"""
1.Write a Python class BankAccount that manages a simple bank account 
  with the following features: 
  Requirements:  
   - Initialize with account number, holder name, and initial balance (default 0)  
   - Implement deposit(amount) method that adds money (must be positive)  
   - Implement withdraw(amount) method that removes money 
     (check sufficient balance)  
   - Implement get_balance() method to return current balance  
   - Implement transfer(amount, target_account) to transfer money to 
     another account 
   -  Maintain transaction history (list of all transactions with type, 
      amount, and timestamp)  
   - Implement __str__() for readable representation
"""
from datetime import datetime

class BankAccount:
  def __init__(self, acc_no, holder_name, initial_balance=0):
   self.acc_no = acc_no
   self.holder_name = holder_name
   self.balance = 0
   self.transaction_history = []
   if initial_balance < 0:
     raise ValueError("An negative balance is invalid !")
   else : 
     self.deposit(initial_balance)

  def deposit(self, amount):
    if amount <= 0 :
      raise ValueError("Deposit value must be positive....!")
    self.balance += amount
    self.add_transaction("DEPOSIT",amount) #(type & amount)..

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError("Withdraw value must be positive....!")
    elif amount > self.balance :
      raise ValueError("Insufficient balance.!!")
    self.balance -= amount
    self.add_transaction("WITHDRAW",amount) 

  def transfer(self, amount, target_account):
    if(not(isinstance(target_account, BankAccount))):
      raise ValueError("Traget account should be BankAccount instance...")
    elif amount <= 0:
      raise ValueError("Transfer value must be positive.....!")
    elif amount > self.balance:
      raise ValueError("Insufficient balance.!!")
    self.balance -= amount
    target_account.balance += amount
    self.add_transaction("TRANSFER_OUT",amount) # transfer history --> Out
    target_account.add_transaction("TRANSFER_IN",amount) # transfer history ---> In

  def get_balance(self):
    return self.balance

  def add_transaction(self, type_, amount):
    self.transaction_history.append({
      "type"       : type_,
      "amount"     : amount,
      "time_stamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      })

  def __str__(self):
    return ( f"BankAccount : (Account no.) {self.acc_no},\n" 
             f"Holder      :               {self.holder_name},\n"
             f"Balance     :               {self.balance}\n" )


acc1 = BankAccount("12345", "Alice", 1000) #(acc_no, holder_name, balance)!
acc2 = BankAccount("67890", "Bob", 500)

acc1.deposit(200)
acc1.withdraw(150)
acc1.transfer(300, acc2)

print(acc1) # checking __str__ method..
print(acc2)

print("\nTransaction History (Alice):")
for txn in acc1.transaction_history:
      print(txn)
print("\nTransaction History (Bob):")
for txn in acc2.transaction_history:
      print(txn)
