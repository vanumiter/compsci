sentence = input("Enter sentence: ")

vowels = ["a", "e", "i", "o", "u"] # spoilers 😳
vowel_count = 0

for char in sentence:
    if char in vowels:
        vowel_count+=1
print("Number of vowels:", vowel_count)