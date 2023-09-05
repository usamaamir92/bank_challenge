from lib.account import *

def test_constructor():
    account = Account()
    assert account.transactions == []
    assert account.balance == 0
    assert account.date == datetime.now().strftime("%d/%m/%Y")