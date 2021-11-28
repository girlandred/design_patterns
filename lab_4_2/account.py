from lab_4_2.customer import Customer


class Account(Customer):
    """
        Represents Account class.

        ...

        Attributes:
        ----------
            account_id : int
                contain account id
            customer_id : int
                customer id
        """

    def __init__(self, acc_id, customer):
        self.id = acc_id
        self.customerId = customer.id


class Checking(Account):
    """
        Represents Checking part.

        ...

        Attributes:
        ----------
            id : int

            account_id : int
                contain account id
        """

    def __init__(self, account):
        self.id = account.id
        self.customerId = account.customerId


class Savings(Account):
    """
        Represents Savings part.

        ...

        Attributes:
        ----------
            id : int

            customer_id : int
                customer id
        """

    def __init__(self, account):
        self.id = account.id
        self.customerId = account.customerId
