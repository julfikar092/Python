# def calc_Average(a, b, c):
#     print((a+b+c)/3)

# calc_Average(8, 5, 46)


# def lenStr(parString):
#     return len(parString)

# co = lenStr([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(co)


# def listPrint(cities):
#     for el in cities:
#         print(el, end=" ")

# cities = ["Dhaka", "Rajshahi", "Rangpur",
#           "Khulna", "Barishal", "Chittagong", "Sylhet"]

# listPrint(cities)


# def fac(n):
#     f = 1
#     for el in range(1, n+1):
#         f = f*el
#     return f

# facto = fac(4)
# print(facto)


# def con(taka):
#     print(taka*123)


# x = int(input("Enter Dollar to convert taka: "))
# con(x)


# def rec(num):
#     if (num == 0):
#         return 0
#     return num + rec(num-1)


# x = int(input("Enter number: "))

# print(rec(x))


def rec(PL, ind):
    if (ind == len(PL)):
        return

    print(PL[ind])

    rec(PL, ind+1)


myList = ["Dhaka", "Rajshahi", "Rangpur",
          "Khulna", "Barishal", "Chittagong", "Sylhet"]

rec(myList, 0)
