message1 = input("Enter your message: ")

messageArry =message1.split(" ")

SecretCode = []
randomwords1 = "glz"
randomwords2 = "htx"

if (len(messageArry)>1):
    for word in messageArry:
        if(len(word)>=3):
            newWord = randomwords1 + word[1:] + word[0] + randomwords2
            SecretCode.append(newWord)
        else:
            SecretCode.append(word[::-1])

    print(" ".join(SecretCode))    

else:
    word=messageArry[0]
    if(len(word)>=3):
        newWord = randomwords1 + word[1:]+word[0]+randomwords2
        SecretCode.append(newWord)
        
    else:
        newWord = word[::-1]
        SecretCode.append(newWord)

    print(" ".join(SecretCode))    

