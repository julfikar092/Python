with open("Innovative Skills/Exam - 1/test4.txt") as file:
    con = file.readlines()

    num = int(con[0].strip())

    list_of_numbers = con[1].strip().split()

    unique_numbers = set(list_of_numbers)

    print(f"Unique Count: {len(unique_numbers)}")
