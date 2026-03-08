with open("Innovative Skills/Exam - 1/test2.txt") as file:
    content = file.readlines()

    A = float(content[0].strip())
    B = float(content[1].strip())
    C = float(content[2].strip())

    average = ((A * 2) + (B * 3) + (C * 5)) / 10

    print(f"MEDIAN = {average:.1f}")
