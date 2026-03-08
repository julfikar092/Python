with open("Innovative Skills/Exam - 1/test5.txt") as file:
    con = file.readlines()

    num = int(con[0].strip())

    list_of_numbers = con[1].strip().split()
    even_list = []
    odd_list = []

    for i in list_of_numbers:
        i = int(i)
        if (i % 2 == 0):
            even_list.append(i)
        else:
            odd_list.append(i)
    print(f"Even: {even_list}\nOdd: {odd_list}")
