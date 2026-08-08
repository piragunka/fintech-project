class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(
            f"Пополнение: {amount:.2f} руб."
        )

    def withdraw(self, amount):
        if amount > self.balance:
            return False

        self.balance -= amount
        self.transactions.append(
            f"Списание: {amount:.2f} руб."
        )

        return True

    def show_balance(self):
        return self.balance

    def show_transactions(self):
        return self.transactions
