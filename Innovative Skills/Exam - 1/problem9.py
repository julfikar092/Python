with open("Innovative Skills/Exam - 1/test9.txt") as file:
    content = file.readlines()

    name = content[0].strip()

    attendance = float(content[1].strip())

    marks = content[2].strip().split()
    total_mark = 0
    grade = ""

    for mark in marks:
        mark = float(mark)
        total_mark += mark

    average = total_mark/len(marks)

    if (attendance >= 75):
        if (average >= 80):
            grade = "A"
        elif (average >= 60):
            grade = "B"
        else:
            grade = "C"
    else:
        if (average >= 80):
            grade = "B"
        else:
            grade = "Fail"

    print(f"Name: {name}\nFinal Grade: {grade}")
