with open("Innovative Skills/Exam - 1/test1.txt") as file:
    content = file.readlines()
    name = content[0].strip()
    salary = float(content[1].strip())
    total_sales = float(content[2].strip())
    comission = (total_sales*15)/100

    total = salary + comission
    print(f"TOTAL = R$ {total:.2f}")
