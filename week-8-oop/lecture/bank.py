def log_method_call(func):
    def wrapper(self, *args, **kwargs):
        print(f"Method {func.__name__} called with args: {args}, kwargs {kwargs}")
        return func(self, *args, **kwargs)

    return wrapper


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @log_method_call
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    @log_method_call
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance


account = BankAccount("Zidan")
account.deposit(100)
account.withdraw(25)
