from lib.account import *

def test_deposit_function():
     account = Account()
     account.deposit(1000)
     assert account.balance == 1000
     assert len(account.transactions) == 1

def test_withdraw_function():
     account = Account()
     account.withdraw(1000)
     assert account.balance == -1000
     assert len(account.transactions) == 1

def test_view_statement_with_no_transactions():
     account = Account()
     assert account.view_statement() == "date || credit || debit || balance\n"

def test_view_statement_with_multiple_transactions():
    account = Account()
    account.deposit(1000)
    account.deposit(2000)
    account.withdraw(500)
    assert account.view_statement() == "date || credit || debit || balance\n05/09/2023 ||  || 500 || 2500\n05/09/2023 || 2000 ||  || 3000\n05/09/2023 || 1000 ||  || 1000\n"

