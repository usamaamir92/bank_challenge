class Transaction():
    def __init__(self, date, credit, debit, closing_balance):
        self.date = date
        self.credit = float(credit) if credit else None
        self.debit = float(debit) if debit else None
        self.closing_balance = float(closing_balance)


    #Function to convert amount input to 2 deciaml places if int or float, else return an empty string
    # to allow correct format in repr method
    def format_amount(self, amount):
        if amount is not None:
            return "{:.2f}".format(amount)
        else:
            return ""
        

    def __repr__(self):
        return f"{self.date} || {self.format_amount(self.credit)} || {self.format_amount(self.debit)} || {self.format_amount(self.closing_balance)}"

