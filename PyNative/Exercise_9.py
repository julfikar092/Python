sentence = "Learning Python is fun!"
vowels = "aeiou"
vowel_counter = 0

for ch in sentence:
    ch.lower()

    if ch in vowels:
        vowel_counter += 1
print(f"Number of vowels: {vowel_counter}")
