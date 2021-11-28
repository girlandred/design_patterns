import copy

from lab_4_2.prototype import IPrototype


class Customer(IPrototype):
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
