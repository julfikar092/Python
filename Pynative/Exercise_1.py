def sum_or_product(num1, num2):
    if (num1*num2) < 1000:
        return num1*num2
    else:
        return num1+num2


result1 = sum_or_product(20, 30)
print(f"The result is {result1}")

result2 = sum_or_product(40, 30)
print(f"The result is {result2}")
