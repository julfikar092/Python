print(f"Printing current and previous number sum in a range(10)")

for num in range(10):
    current_num = num
    prev_num = num-1 if num >= 1 else 0
    sum = current_num+prev_num

    print(
        f"Current Number {current_num} Previous Number {prev_num} Sum: {sum}")
