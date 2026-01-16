# myTup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# idx = 0

# x = int(input("Searching number: "))

# while i < len(myTup):
#     if (myTup[i] == x):
#         print("number", x, "found!")
#         break
#     else:
#         print("finding..")
#     i += 1

# for el in myTup:
#     if el == x:
#         print("found", el, "at ", idx)
#         break
#     else:
#         print("finding..")
#     idx += 1

# x = int(input("Enter a number for multipliclation: "))
# for num in range(1, 11, 1):

#     print(num*x)


# x = int(input("Enter Number: "))
# sum = 0
# i = 1
# while i <= x:
#     sum = sum + i
#     i += 1
# print(sum)


# x = int(input("Enter Number: "))
# sum = 0

# for num in range(1, x+1, 1):
#     sum += num

# print(sum)

x = int(input("Enter Number: "))
fac = 1

for el in range(x, 0, -1):
    fac *= el

print(fac)
