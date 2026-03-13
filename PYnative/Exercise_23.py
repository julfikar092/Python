def palindrom_checker(num):
    temp = num
    reverse_num = 0
    while (temp > 0):
        reminder = temp % 10
        reverse_num = (reverse_num*10) + reminder
        temp = temp // 10

    if (num == reverse_num):
        return "Palindrom"
    else:
        return "Not Palindrom"


num = 121
result = palindrom_checker(num)
print(result)
