sentence = input("Enter a sentence: ")

# converting to lowercase so 'A' and 'a' counts at the same time
sentence = sentence.lower()

frequency = {}

for char in sentence:
    if char.isalpha():# count only letters
        frequency [char] = frequency.get(char, 0) + 1

# This part shows the result
for letter, count in frequency.items():
    print (f"{letter}: {count}")