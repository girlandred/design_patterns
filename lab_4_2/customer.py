import copy

from lab_4_2.prototype import IPrototype


class Customer(IPrototype):
    """
    Represents Customer

    ...

    Attributes:
    ----------
        id : int
            customer's id.
        name : str
            customer's name.
        address : str
            information about customer's address.
        phone_number : str
            contain phone number.
        initial_amount : int
            balance

    Methods:
    --------

        general_inquiry()

        deposit()
            Ability to transfer money into credit card.
        withdraw()
            Ability to withdraw money from credit card.
        open_account()
            Creating new account in the bank.
        close_account()
            Deleting account in the bank.
        apply_for_loan()
            Inquiry for a loan.
        request_card()

        clone()
            Implementation of prototype pattern
        """

    def __init__(self, _id, name, address, phone_number, account_number, initial_amount):
        self.id = _id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.no = account_number
        self.balance = initial_amount

    def general_inquiry(self):
        pass

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def open_account(self, customer):
        return customer

    def close_account(self):
        pass

    def apply_for_loan(self):
        pass

    def request_card(self):
        pass

    def clone(self):
        return copy.deepcopy(self)
