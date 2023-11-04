text = str.lower(input("Enter text: "))
key = int(input("Enter how many letters the text should be shifted: "))

ascii = []
for i in range(len(text)):
    ascii.append(ord(text[i])+key)
# Converts each letter of the table "char" to an ASCII decimal + the key and adds them to table "ascii"

encrypt = ""
for i in range(len(ascii)):
    encrypt += chr(ascii[i])
# Converts the shifted ASCII decimals from table "ascii" into plain text and adds them to string "encrypt"

print(encrypt)