from lib.account import *
from lib.transaction import *
import pytest
from unittest.mock import *


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

    account.get_current_date = Mock(return_value="05/09/2023")

    account.deposit(1000.00)
    account.deposit(2000.00)
    account.withdraw(500.00)

    assert account.view_statement() == (
    "date || credit || debit || balance\n"
    "05/09/2023 ||  || 500.00 || 2500.00\n"
    "05/09/2023 || 2000.00 ||  || 3000.00\n"
    "05/09/2023 || 1000.00 ||  || 1000.00\n")

    
def test_non_integer_or_float_deposit_inputs_throw_error():
     with pytest.raises(Exception) as e:
        account = Account()
        account.deposit("Hello")
     error_message = str(e.value)
     assert error_message == "Amount must be a number"

def test_non_integer_or_float_withdrawal_inputs_throw_error():
     with pytest.raises(Exception) as e:
        account = Account()
        account.withdraw("Hello")
     error_message = str(e.value)
     assert error_message == "Amount must be a number"
          
