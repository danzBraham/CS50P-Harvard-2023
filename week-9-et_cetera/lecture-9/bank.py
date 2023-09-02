class Account:
    def __init__(self, balance=0):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def deposit(self, n):
        self.balance += n

    def withdraw(self, n):
        self.balance -= n


def main():
    account = Account()
    print(f"Balance: {account.balance}")
    account.deposit(100)
    account.withdraw(75)
    print(f"Balance: {account.balance}")


if __name__ == "__main__":
    main()
