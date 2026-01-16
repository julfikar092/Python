even_sum = 0
odd_sum = 0
for i in range(1,11):
    if (i%2 == 1):
        odd_sum = odd_sum + i
    else:
        even_sum = even_sum + i

print("Sum of even: ",even_sum)
print("Sum of odd: ",odd_sum)