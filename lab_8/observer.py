from __future__ import annotations

from typing import List
import hashlib
from abc import ABC, abstractmethod
import mysql.connector

cnx = mysql.connector.connect(user='root', password='12345',
                              host='localhost',
                              database='test_schema')
cursor = cnx.cursor()


class IAcct(ABC):
    @abstractmethod
    def get_balance(self) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: int) -> bool:
        pass

    @abstractmethod
    def attach(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def detach(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Account(IAcct):
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return print(f'Your balance {self.balance}')

    def withdraw(self, amount: int) -> bool:
        if amount < 0:
            return False
        else:
            print(f'You can withdraw money')
            return True

    def attach(self, customer: Customer) -> None:
        pass

    def detach(self, customer: Customer) -> None:
        pass

    def notify(self) -> None:
        pass


class AccountProxy(IAcct):
    def __init__(self, balance, ad: AccountDatabase, account: Account) -> None:
        self.ad = ad
        self._account = account
        self._balance = balance

    _customers: List[Customer] = []

    def withdraw(self, amount: int) -> bool:
        return False

    def get_balance(self) -> None:
        if not self.ad.login():
            return self._account.get_balance()

    def attach(self, customer: Customer) -> None:
        print("Customer was attached")
        self._customers.append(customer)

    def detach(self, customer: Customer) -> None:
        print("Customer was detached")
        self._customers.remove(customer)

    def notify(self) -> None:
        print("Customers was notified")


class Customer:
    def __init__(self, name, id_cust, account_number, account: Account):
        self.name = name
        self.id_cust = id_cust
        self.account_number = account_number
        self._account = account

    def withdraw(self, amount: int) -> bool:
        return False

    def update(self, account: Account) -> None:
        if account.get_balance():
            print("Reacted to the event")


class IDB(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass


class AccountDatabase(IDB):
    def __init__(self, a: Account):
        self.a = a
        self.acc_id = input('Account id: ')
        self.name = input('Name: ')
        self.password = input('Password: ')
        self.hash_pass = hashlib.md5(self.password.encode("utf-8")).hexdigest()

    def login(self):
        return print(f"You are logged in: {self.acc_id}")

    def logout(self):
        return print("You are logged out")


class DatabaseProxy(IDB):
    def __init__(self, acc: AccountDatabase) -> None:
        self._acc = acc

    def login(self):
        add_account = "INSERT INTO accounts(acc_id, name, password) VALUES (%s, %s, %s)"
        values = (self._acc.acc_id, self._acc.name, self._acc.hash_pass)
        cursor.execute(add_account, values)
        cnx.commit()

    def logout(self):
        cursor.close()
        cnx.close()

    def make_acc_proxy(self):
        return self._acc


class ATM:
    def __init__(self, acc_id, ad: AccountDatabase):
        self.acc_id = acc_id
        self.ad = ad

    def handle_balance_request(self, balance):
        pass

    def handle_login(self):
        if self.acc_id == self.ad.login():
            return True
        else:
            return False

    def handle_logout(self):
        pass

    def handle_withdraw(self):
        pass


def client_code(idb: IDB) -> None:
    idb.login()
    idb.logout()


def client_code2(iacct: IAcct) -> None:
    iacct.get_balance()
    iacct.withdraw(amount=13)


if __name__ == "__main__":
    # The client code.
    a = Account(balance=1234567)
    # print("Client: Executing the client code with a real subject:")
    ad = AccountDatabase(a=a)
    # client_code(ad)

    print("")
    dab = DatabaseProxy(ad)
    # client_code(dab)

    print("")
    acc_prox = AccountProxy(account=a, ad=ad, balance=a.balance)
    # client_code2(acc_prox)

    atm = ATM(ad=ad, acc_id='')
    customer = Customer('Anton', 12, 23, a)

    acc_prox.attach(customer)

    acc_prox.get_balance()

    acc_prox.detach(customer)
