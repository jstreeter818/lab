import pytest
from account import *


class Test:
    def setup_method(self):
        self.account1 = Account('Jane')
        self.account2 = Account('John')

    def teardown_method(self):
        del self.account1
        del self.account2

    def test_init(self):
        assert self.account1.get_name() == 'Jane'
        assert self.account1.get_balance() == 0
        assert self.account2.get_name() == 'John'
        assert self.account2.get_balance() == 0

    def test_deposit(self):
        assert self.account1.deposit(5) is True
        assert self.account2.deposit(5.25) is True
        assert self.account1.get_balance() == 5
        assert self.account2.get_balance() == 5.25
        assert self.account1.deposit(0) is False
        assert self.account2.deposit(-5) is False
        assert self.account1.get_balance() == 5
        assert self.account2.get_balance() == 5.25

    def test_withdraw(self):
        self.account1.deposit(10)
        self.account2.deposit(5.50)

        assert self.account1.withdraw(5) is True
        assert self.account2.withdraw(2.25) is True
        assert self.account1.get_balance() == 5
        assert self.account2.get_balance() == 3.25
        assert self.account1.withdraw(10) is False
        assert self.account2.withdraw(5.50) is False
        assert self.account1.get_balance() == 5
        assert self.account2.get_balance() == 3.25
