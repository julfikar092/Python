def reverse_digit(num):

    reversed_number = ""
    while (num > 0):
        reminder = num % 10
        num = num//10
        reversed_number = reversed_number+str(reminder)

    return reversed_number


num = 7536

print(reverse_digit(num))
