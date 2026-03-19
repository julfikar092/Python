fibonacci_series_number = 15

num1 = 0
num2 = 1

for n in range(fibonacci_series_number):
    print(num1, end=" ")
    num3 = num1 + num2
    num1 = num2
    num2 = num3
