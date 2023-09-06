from lib.account import *
from lib.transaction import *
from unittest.mock import *


def test_deposit_function():
     account = Account()
     
     # Mocking datetime function to fixed date
     fixed_date = "05/09/2023"
     with patch.object(account, 'get_current_date', return_value=fixed_date):
          account.deposit(1000)
     
     assert account.balance == 1000
     assert len(account.transactions) == 1

     transaction = account.transactions[0]
     assert transaction.date == fixed_date
     assert transaction.credit == 1000
     assert transaction.debit == None
     assert transaction.closing_balance == 1000
     assert str(account.transactions[0]) == "05/09/2023 || 1000.00 ||  || 1000.00"



def test_withdraw_function():
     account = Account()

     # Mocking datetime function to fixed date
     fixed_date = "05/09/2023"
     with patch.object(account, 'get_current_date', return_value=fixed_date):
          account.withdraw(1000)
     
     assert account.balance == -1000
     assert len(account.transactions) == 1

     transaction = account.transactions[0]
     assert transaction.date == fixed_date
     assert transaction.credit == None
     assert transaction.debit == 1000
     assert transaction.closing_balance == -1000
     assert str(account.transactions[0]) == "05/09/2023 ||  || 1000.00 || -1000.00"



def test_view_statement_with_no_transactions():
     account = Account()
     assert account.view_statement() == "date || credit || debit || balance\n"


def test_view_statement_with_multiple_transactions():
    account = Account()

    account.get_current_date = Mock(return_value="05/09/2023")

    account.deposit(1000.00)
    account.deposit(2000.00)
    account.withdraw(500.00)

    assert account.view_statement() == (
    "date || credit || debit || balance\n"
    "05/09/2023 ||  || 500.00 || 2500.00\n"
    "05/09/2023 || 2000.00 ||  || 3000.00\n"
    "05/09/2023 || 1000.00 ||  || 1000.00\n")
          
