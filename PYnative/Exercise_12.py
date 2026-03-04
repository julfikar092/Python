def calculate_result(numbers):
    if numbers[0] == numbers[len(numbers)-1]:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
result1 = calculate_result(numbers_x)
result2 = calculate_result(numbers_y)

print(f"Given list: {numbers_x} | result is {result1}")
print(f"Given list: {numbers_y} | result is {result2}")
