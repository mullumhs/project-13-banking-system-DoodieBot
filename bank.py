""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Personal_Account

class BankManager:
    def __init__(self):
        self.account=[]
     
    def existing_account(self, acc_no):
        for account in self._account:
            if account.get_acc_no() == acc_no:
                return account
        return False
    
    def add_account(Self, new_account):
        if new_account == Self.existing_account:
            raise ValueError("no bueno")
        else:
            Self.account.append(new_account) 