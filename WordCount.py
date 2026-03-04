with open("words.txt", "r") as f:
    data = f.read()

    print(len(data))

    word = ""
    count = 0

    for ch in data:
        if ch == " " or ch == "\n":
            if word != "":
                print(word)
                count += 1
                word = ""
        else:
            word += ch

    if word != "":
        print(word)
        count += 1

    print(count)
