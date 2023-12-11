sentence = input("Enter sentence: ")
letter = input("Choose letter: ")
letter_count = 0

for chars in sentence:
    if chars == letter:
        letter_count+=1

print("Times occured: " + str(letter_count))