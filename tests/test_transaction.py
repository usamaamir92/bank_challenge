from lib.transaction import *

def test_constructor():
    transaction = Transaction("01/01/2000", 0, 200, 1000)
    assert transaction.date == "01/01/2000"
    assert transaction.credit == 0
    assert transaction.debit == 200
    assert transaction.closing_balance == 1000


def test_repr_function():
    transaction = Transaction("01/01/2000", 0, 200, 1000)
    assert repr(transaction) == "01/01/2000 || 0 || 200 || 1000"