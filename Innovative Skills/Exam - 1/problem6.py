with open("Innovative Skills/Exam - 1/test6.txt") as file:
    content = file.readlines()

    list_of_words = content[0].strip().split()

    word_count = {}

    for word in list_of_words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_word = dict(sorted(word_count.items()))

    for word in sorted_word:
        print(f"{word}: {sorted_word[word]}")
