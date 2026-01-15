# class student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def avr(self):
#         avg = (self.marks[0]+self.marks[1]+self.marks[2])/3
#         # for value in self.marks:
#         #     sum += value
#         print(self.name, "Your average is: ", avg)


# s1 = student("Julfikar", [66, 77, 55])
# s1.avr()


class Account:

    def __init__(self, balance, account):
        self.balance = balance
        self.account = account

    def debit(self, amount):
        self.balance -= amount
        print("Debited", amount, "taka. Now your balance is ", self.balance, "taka")

    def credit(self, amount):
        self.balance += amount
        print("Debited", amount, "taka. Now your balance is ", self.balance, "taka")

    def print(self):
        print("Total Amount of Money", self.balance)


A = Account(30000, 1236485636487)
A.debit(5200)
A.credit(9822)
A.print()
