""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Personal_Account

class BankManager:
    def __init__(self):
        self._accounts=[]
     
    def existing_account(self, acc_no):
        for account in self._accounts:
            if account.get_acc_no() == acc_no:
                return account
        return False
    
    def add_account(self, new_account_no, new_account_name):
        new_account = self.existing_account(new_account_no)
        if new_account:
            raise ValueError("account already exists")
        else:            
            self._accounts.append(Personal_Account(new_account_name, new_account_no, 0))
            print("account sucsefully created")
        
        
        
        
        
        
man1 = BankManager()

man1.add_account("david","1234")