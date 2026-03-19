def exponent(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result


print(exponent(2, 5))
