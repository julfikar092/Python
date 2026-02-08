# Ques - 1️: Take Student Information

name = input("Enter Name: ")
age = int(input("Enter age: "))

english_number = float(input("Enter Number of English: "))
math_number = float(input("Enter Number of Math: "))
science_number = float(input("Enter Number of Science: "))

# Ques - 2️: Store the Data

student_info = [name, age]
student_marks = (english_number,math_number,science_number)

print(student_info)
print(student_marks)

# Ques - 3️: Calculate Result

total_marks = english_number+math_number+science_number
average = total_marks/3

if average>40: 
    print("Pass")
else:
    print("Pass")

# Ques - 4: Simple String Operations

name_upper = name.upper()
name_lower = name.lower()
reverse_name = name[::-1]

print(reverse_name)

# Ques - 5: Simple List Operation

phone = input("Eneter Phone Number: ")
student_info.append(phone)

print(student_info)