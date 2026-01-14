message = input("Enter your message: ")

words= message.split(" ")

print("Encoded Message: \n")
nWord=[]
r1="ewx"
r2= "krl"
if(len(words)==1):
    for word in words:
        if(len(word)<3):
            nWord = word[::-1]
        else:
            nWord=r1+word[1:]+word[0]+r2
    print(nWord)
else:
    for word in words:
        if(len(word)<3):
            nWord = word[::-1]
        else:
            nWord=r1+word[1:]+word[0]+r2

print("\nDecoded Message: \n")