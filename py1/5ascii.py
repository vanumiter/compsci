import time

characters = []
iteration = 1
for i in range(1,6):
    char = input(f"Enter character {iteration}: ")
    if len(char) != 1:
        print("Please enter only one character.")
        exit()
    else:
        characters.append(char)
        iteration += 1
# Enters the inputted characters individually 5 times into the list "characters"

ascii = [ord(char) for char in characters]
# Gets the ascii decimal value for each element in "characters", which is put into the list "ascii"

print("The characters you have used are:", characters)
time.sleep(1) # cool
print(f"The ASCII decimal values of the characters respectively are:", ascii)


