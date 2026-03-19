
prime_numbers = []
for num in range(2, 21):
    for j in range(2, (num//2 + 1)):
        if (num % j == 0):
            break
    else:
        prime_numbers.append(num)

alternative_prime = prime_numbers[::2]
print(alternative_prime)
