text = "apple banana apple cherry banana apple"

text_list = text.split()

frequency = {}

for word in text_list:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)
