from datetime import datetime

class Account():
    def __init__(self):
        self.transactions = []
        self.balance = 0
        self.date = datetime.now().strftime("%d/%m/%Y")