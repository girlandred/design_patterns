from lab_4_2.customer import Customer


class Loan(Customer):
    def __init__(self, loan_id, loan_type, account, customer):
        self.id = loan_id
        self.type = loan_type
        self.acc_id = account.id
        self.customerId = customer.id
