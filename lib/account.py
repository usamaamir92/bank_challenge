from datetime import datetime
from lib.transaction import *

class Account():
    def __init__(self):
        self.transactions = []
        self.balance = 0

    def get_current_date(self):
        return datetime.now().strftime("%d/%m/%Y")

    def deposit(self, amount):
        if type(amount) != int and type(amount) != float:
            raise Exception("Amount must be a number")
        self.balance += amount
        transaction = Transaction(self.get_current_date(), amount, None, self.balance)
        self.transactions.insert(0, transaction)


    def withdraw(self,amount):
        if type(amount) != int and type(amount) != float:
            raise Exception("Amount must be a number")
        self.balance -= amount
        transaction = Transaction(self.get_current_date(), None, amount, self.balance)
        self.transactions.insert(0, transaction)


    def view_statement(self):
        statement = "date || credit || debit || balance\n"
        for transaction in self.transactions:
            statement += f"{transaction}\n"
        return statement

    