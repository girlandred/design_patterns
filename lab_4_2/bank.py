class Bank(object):
    def __init__(self, bankID, name, location):
        self.bankId = bankID
        self.name = name
        self.location = location
        self.customer_list = []
