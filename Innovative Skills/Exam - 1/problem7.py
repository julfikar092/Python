class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(
                f"You have only {self.balance:.2f}. Please try different amount")
            return

    def display_balance(self):
        print(f"Final Balance: {self.balance:.2f}")


with open('Innovative Skills/Exam - 1/test7.txt') as file:
    content = file.readlines()

    name = content[0].strip()
    initial_balance = float(content[1].strip())
    num_transactions = int(content[2].strip())

    account = BankAccount(name, initial_balance)

    for i in range(num_transactions):

        transaction = content[3 + i].strip().split()
        transaction_type = transaction[0].lower()
        transaction_amount = float(transaction[1])

        if transaction_type == "deposit":
            account.deposit(transaction_amount)
        elif transaction_type == "withdraw":
            account.withdraw(transaction_amount)

    account.display_balance()
