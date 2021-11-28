from lab_4_2.customer import Customer


class Account(Customer):
    def __init__(self, acc_id, customer):
        self.id = acc_id
        self.customerId = customer.id


class Checking(Account):
    def __init__(self, account):
        self.id = account.id
        self.customerId = account.customerId


class Savings(Account):
    def __init__(self, account):
        self.id = account.id
        self.customerId = account.customerId
