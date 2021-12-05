import hashlib
import json
from dataclasses import dataclass


@dataclass
class PersonalInfo:
    """
        Represents personal information.

        ...

        Attributes:
        ----------
            id : int
                personal id
            name : str
                name of person.
            address : str
                person's address.
            phone_number : str
                show person's phone number.
            email : str
                contain data about email.

        """

    id: int
    name: str
    address: str
    phone_number: str
    email: str


class CreditCard:
    """
        Represents credit card information.

        ...

        Attributes:
        ----------
            client : str
                clients name.
            account_number : int
                number of client's account.
            credit_limit : int
                possible amount of credit.
            grace_period : int

            cvv : str
                cvv.

        Methods:
        --------

        give_bank_details()
            Return information about bank.

        """
    def __init__(self, client, account_number,
                 credit_limit, grace_period, cvv):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv = cvv

    def give_bank_details(self, *args):
        return json.dumps(self, default=lambda o: bank_info.__dict__)

    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        encode = hashlib.md5(cvv.encode())
        cvv = encode.hexdigest()
        self._cvv = cvv

    def order_card(self):
        pass


class CustomizedCard(CreditCard):
    """
        Represents specific credit cards, decorator class.

        ...
        Methods:
        --------

        order_card()
            Ordering customized credit card.

        """
    def __init__(self, client, account_number, credit_limit, grace_period, cvv):
        super().__init__(client, account_number, credit_limit, grace_period, cvv)

    _credit_card: CreditCard = None

    @property
    def credit_card(self):
        return self._credit_card

    def order_card(self):
        return self._credit_card.order_card()


class GoldenCreditCard(CustomizedCard):
    """
        Represents golden credit card.

        ...
        Methods:
        --------

        order_card()
            Ordering golden credit card.

        """
    def order_card(self):
        return print(f"Golden credit card was issued")


class CorporateCreditCard(CustomizedCard):
    """
        Represents corporate credit card.

        ...
        Methods:
        --------

        order_card()
            Ordering corporate credit card.

        """
    def order_card(self):
        return print(f"Corporate credit card was issued")


class BankInfo:
    """
        Represents bank information.

        ...

        Attributes:
        ----------
            bank_name : str
                bank's name.
            holder_name : str
                holder's name.
            credit_card : CreditCard
                contain credit card information.

        Methods:
        --------

        transaction_list()
            Array of transactions made by specific account.

        """

    def __init__(self, bank_name, holder_name, credit_card: CreditCard):
        self.account_number = credit_card.account_number
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = []
        self.credit_history = []

    def transaction_list(self):
        return self.accounts_number.append(self.account_number)


class BankCustomer:
    """
        Represents bank customer's information.

        ...

        Attributes:
        ----------
            credit_card : CreditCard
                credit card details.
            personal_info : PersonalInfo
                personal info details.

        Methods:
        --------

        give_bank_details()
            Return information about bank.

        """

    def __init__(self, credit_card, personal_info=PersonalInfo):
        self.credit_card = credit_card
        self._personal_info = personal_info

    def give_bank_details(self, *args):
        return json.loads(credit_card.give_bank_details())

    @property
    def personal_info(self):
        return self._personal_info

    @personal_info.setter
    def personal_info(self, _personal_info: PersonalInfo):
        if isinstance(_personal_info, PersonalInfo):
            self._personal_info = PersonalInfo
        else:
            raise AttributeError(f"personal_info object must be of class Personal info")


def client_code(bank_customer: "BankCustomer"):
    print(bank_customer.give_bank_details())


credit_card = CreditCard("Maryna", 535, 2772, 7277, 736)

bank_info = BankInfo("Hilton Bank", "Robertson Patricio", credit_card=credit_card)
bank_info.transaction_list()
bank_customer = BankCustomer(credit_card=credit_card)

info = json.dumps(credit_card.give_bank_details())
client_code(bank_customer=bank_customer)


gold_card = GoldenCreditCard("Maryna", 535, 2772, 7277, 736)
corp_card = CorporateCreditCard("Maryna", 535, 2772, 7277, 736)
gold_card.order_card()
corp_card.order_card()
