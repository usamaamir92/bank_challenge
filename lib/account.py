from datetime import datetime
from lib.transaction import *

class Account():
    def __init__(self):
        self.transactions = []
        self.balance = 0
        self.date = datetime.now().strftime("%d/%m/%Y")


    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction(datetime.now().strftime("%d/%m/%Y"), amount, "", self.balance)
        self.transactions.insert(0, transaction)


    def withdraw(self,amount):
        self.balance -= amount
        transaction = Transaction(datetime.now().strftime("%d/%m/%Y"), "", amount, self.balance)
        self.transactions.insert(0, transaction)


    def view_statement(self):
        statement = "date || credit || debit || balance\n"
        for transaction in self.transactions:
            statement += f"{str(transaction)}\n"
        print(statement)
        return statement

    