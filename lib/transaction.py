

class Transaction():
    def __init__(self, date, credit, debit, closing_balance):
        self.date = date
        self.credit = credit
        self.debit = debit
        self.closing_balance = closing_balance

    def __repr__(self):
        return f"{self.date} || {self.credit} || {self.debit} || {self.closing_balance}"

