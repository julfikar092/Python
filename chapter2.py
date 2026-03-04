str = "Hello, World!"
print(len(str))

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
number3 = int(input("Enter third number:"))

if (number1 >= number2 and number1 >= number3):
    print("Number 1 is the greatest")
elif (number2 >= number3 and number2 >= number1):
    print("Number 2 is the greatest")
elif (number3 >= number1 and number3 >= number2):
    print("Number 3 is the greatest")
else:
    print("All numbers are equal")
