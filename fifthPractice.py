
list= [1,4,9,16,25,36,49,64,81,100]

se = int(input("Enter Search item: "))

for item in list:
    if(item==se):
        print("found ", se)
        break
    else:
        print("Founding...")
else:
    print("Not found")