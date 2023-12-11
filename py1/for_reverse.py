sentence = input("Enter sentence: ")
sentence_reverse = ""

# -1 used in first argument because in a string, last index number = number of characters - 1
# -1 used in second argument so that chars reach the 0th index of the sentence
for chars in range(len(sentence)-1, -1, -1):
    sentence_reverse += sentence[chars]

print("Reversal of sentence:", sentence_reverse)