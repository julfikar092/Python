# with open("new.tst", "a") as f:
#     f.write("How are you labonno?")
#     f.write("\nI am waiting")
#     f.write("\nI love java")
#     f.write("\njava is my favorite course")


# with open("new.tst", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("new.tst", "w") as f:
#     f.write(new_data)


# with open("new.tst", "r") as f:
#     data = f.read()

# if (data.find("waiting") != -1):
#     print("Existis")
# else:
#     print("Not")

# def first_Occur():
#     word = "waiting"
#     data = True
#     line_No = 1
#     with open("new.tst", "r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 # print("Found in ", line_No)
#                 return line_No
#             line_No += 1
#     return -1


# print(first_Occur())

# def stringOccur():
#     linecount = 1
#     word = "learning"
#     data = True
#     with open("demo.txt", "r") as f:
#         while data:
#             chekcData = f.readline()
#             if (word in chekcData):
#                 print("Data is present in ", linecount)
#                 return linecount
#             linecount += 1
#     return -1


# val = stringOccur()

# print(val)

# def findLine():
#     word = "learning"
#     lineCount = 1
#     data = True
#     with open("demo.txt", "r") as f:
#         while data:
#             data = f.readline()

#             if (word in data):
#                 print(lineCount)
#                 return
#             lineCount += 1

#     return -1


# findLine()


# with open("data.txt", "r") as f:
#     data = f.read()
#     print(data)
#     print(type(data))

#     numbers = data.split(",")
#     evenCount = 0
#     for num in numbers:
#         num = int(num)
#         if num % 2 == 0:
#             evenCount += 1
#     print(evenCount)
