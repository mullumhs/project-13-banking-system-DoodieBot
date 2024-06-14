""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Personal_Account:
    def __init__(self, name, acc_no, balance,):
        self.set_name=name
        self.set_acc_no(acc_no)
        self.set_balance()
    
    def get_name(self):
        return self._name
        
    def set_acc_no(self, new_acc_no):
        if new_acc_no == "":
            raise ValueError("an account number must be created.")
        self._acc_no = new_acc_no
    
    def get_acc_no(self):
        return self._acc_no
        
    def set_balance(self, new_balance):
        if new_balance<0:
            raise ValueError("Balance can not be negative.")
        self._balance = new_balance
        
    def get_balance(self):
        return self._balance