def check_palindrom(num):
    original_number = str(num)
    rev_number = original_number[::-1]

    if original_number == rev_number:
        print(f"Number {original_number} is a palindrome number")
    else:
        print(f"Number {original_number} is not palindrome number")


check_palindrom(121)
check_palindrom(125)
