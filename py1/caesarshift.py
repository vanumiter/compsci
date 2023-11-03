text = str.lower(input("Enter text: "))
key = int(input("Enter how many letters the text should be shifted: "))

chars = []
for i in range(len(text)):
    chars.append(text[i])
# Adds each letter of text to table "char"

ascii = []
for i in range(len(chars)):
    ascii.append(ord(chars[i])+key)
# Converts each letter of the table "char" to an ASCII decimal + the key and adds them to table "ascii"

encrypt = ""
for i in range(len(ascii)):
    encrypt += chr(ascii[i])
# Converts the shifted ASCII decimals from table "ascii" into plain text and adds them to string "encrypt"

print(encrypt)