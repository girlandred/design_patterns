from lab_4_2.customer import Customer


class Loan(Customer):
    """
    Represents Loan

    ...

    Attributes:
    ----------
        loan_id : int
            loan id.
        type : str
            loan's type.
        acc_id : int
            information about account id.
        customerId : int
            contain customer's id.

    """

    def __init__(self, loan_id, loan_type, account, customer):
        self.id = loan_id
        self.type = loan_type
        self.acc_id = account.id
        self.customerId = customer.id
