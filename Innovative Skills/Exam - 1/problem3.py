with open("Innovative Skills/Exam - 1/test3.txt") as file:
    con = file.readlines()

    name = con[0].strip()
    num1 = float(con[1].strip())
    num2 = float(con[2].strip())
    num3 = float(con[3].strip())

    av = (num1+num2+num3)/3
    grade = ""

    if (av >= 80):
        grade = "A"
    elif (av >= 60 and av < 80):
        grade = "B"
    elif (av >= 40 and av < 60):
        grade = "C"
    else:
        grade = "Fail"

    print(f"Name: {name}\nAverage: {av:.2f}\nGrade: {grade}")
