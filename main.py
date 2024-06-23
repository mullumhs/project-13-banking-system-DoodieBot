""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: main.py
# Description: Contains the user interface for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from bank import BankManager
from account import Personal_Account
  

def add_acc_ui(bank):
    name = input("Enter your Name: ")
    acc_no = input("Enter the randomised 4 digit bank identifacation number:")