income = 45000

payable_tax = 0

if income < 10000:
    payable_tax = 0
elif income < 20000 and income >= 10000:
    payable_tax = ((income-10000)*10)/100
else:
    payable_tax = ((10000*10)/100) + (((income-20000)*20)/100)

print(f"Payable income tax = {payable_tax}")
