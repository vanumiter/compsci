choose = input("Type \"1\" to convert a character to an ASCII decimal value.\nType \"2\" to convert an ASCII decimal value to a character.\nEnter a number: ")

def character_to_ascii():
    try:
        character = str(input("Enter a character here: "))
        ascii = ord(character)
        print("The ASCII decimal value of", character, "is", ascii)
    except ValueError:
        print("Please choose a valid character.")

def ascii_to_character():
    try:
        ascii = int(input("Enter an ASCII decimal value here: "))
        character = chr(ascii)
        print("The character of the decimal value", ascii, "is", character)
    except ValueError:
        print("Please choose a valid number.")

try:
    choose = int(choose)
    if choose == 1:
        character_to_ascii()
    elif choose == 2:
        ascii_to_character()
except ValueError:
    print("Please choose a valid number.")
    

