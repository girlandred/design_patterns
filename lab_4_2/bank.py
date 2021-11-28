class Bank(object):
    """
        Represents Bank class.

        ...

        Attributes:
        ----------
            bankId : int
                id of the bank.
            name : string
                name of the bank.
            location : string
                information about bank location.
            customer_list : []
                contain customers.

        """
    def __init__(self, bankID, name, location):
        self.bankId = bankID
        self.name = name
        self.location = location
        self.customer_list = []
