numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]

even_num = []
odd_num = []

for i in range(len(numbers)):
    if (numbers[i] % 2 == 0):
        even_num.append(numbers[i])
    else:
        odd_num.append(numbers[i])


print(even_num)
print(odd_num)
