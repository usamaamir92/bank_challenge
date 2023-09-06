from lib.account import *
from unittest.mock import *


def test_constructor():
    account = Account()
    assert account.transactions == []
    assert account.balance == 0

def transaction_mock(date, credit, debit, closing_balance):
    return {
        'date': date,
        'credit': credit,
        'debit': debit,
        'closing_balance': closing_balance,
    }


@patch('lib.transaction.Transaction', transaction_mock)
def test_deposit_function():
    account = Account()

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


@patch('lib.transaction.Transaction', transaction_mock)
def test_withdraw_function():
    account = Account()

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


@patch('lib.transaction.Transaction', transaction_mock)
def test_view_statement_function():
    account = Account()

    fixed_date = "05/09/2023"
    with patch.object(account, 'get_current_date', return_value=fixed_date):
        account.deposit(2000)
        account.withdraw(500)


    assert account.view_statement() == (
    "date || credit || debit || balance\n"
    "05/09/2023 ||  || 500.00 || 1500.00\n"
    "05/09/2023 || 2000.00 ||  || 2000.00\n")