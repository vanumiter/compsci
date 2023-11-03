text = str.lower(input("Enter text: "))
key = int(input("Enter how many letters the text should be shifted: "))


x = 0
chars = []
for i in range(len(text)):
    chars.append(text[x])
    x+=1
# Adds each letter of text to table "char"

y = 0
ascii = []
for i in range(len(chars)):
    ascii.append(ord(chars[y])+key)
    y+=1
# Converts each letter of the table "char" to an ASCII decimal + the key and adds them to table "ascii"

z = 0
encrypt = ""
for i in range(len(ascii)):
    encrypt += chr(ascii[z])
    z+=1
# Converts the shifted ASCII decimals from table "ascii" into plain text and adds them to string "encrypt"

print(encrypt)