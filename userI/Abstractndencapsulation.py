from abc import ABC, abstractmethod

# Abstract Class
class BankAccount(ABC):

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance      # Private Attribute

    # Encapsulation Methods
    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    # Abstract Method
    @abstractmethod
    def show_details(self):
        pass


# Child Class
class SavingsAccount(BankAccount):

    def show_details(self):
        print("Account Holder :", self.account_holder)
        print("Balance :", self.get_balance())


# Creating Object
account = SavingsAccount("Varsha", 5000)

# Controlled Access
account.deposit(2000)

# Display Details
account.show_details()