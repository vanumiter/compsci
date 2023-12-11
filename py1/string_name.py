fullname = input("Enter your full name: ")

space = fullname.index(" ")

forename = fullname[:space]
surname = fullname[space+1:]
#output without +1: Your forename is water and your surname is  melon.
#output with +1: Your forename is water and your surname is melon.
#Note the extra space created by slicing/substringing the space within the surname.

print("Your forename is", forename, "and your surname is", surname+".")