from lib.transaction import *

def test_constructor():
    transaction = Transaction("01/01/2000", None, 200, 1000)
    assert transaction.date == "01/01/2000"
    # assert transaction.credit == 0.00
    assert transaction.debit == 200.00
    assert transaction.closing_balance == 1000.00


def test_repr_function():
    transaction = Transaction("01/01/2000", 0.00, 200.00, 1000.00)
    assert repr(transaction) == "01/01/2000 ||  || 200.00 || 1000.00"