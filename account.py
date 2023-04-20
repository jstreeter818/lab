class Account:
    """
    A class representing a person's bank account
    """

    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of an Account object
        :param name: name of account owner
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to deposit money to account balance
        :param amount: amount added to account balance
        :return: True if deposit is successful, False if unsuccessful
        """
        self.get_balance()
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Method to withdraw money from account balance
        :param amount: amount removed from account balance
        :return: True if withdraw is successful, False if unsuccessful
        """
        self.get_balance()
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Method to retrieve account's balance
        :return: account's balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to retrieve account owner's name
        :return: owner's name
        """
        return self.__account_name
