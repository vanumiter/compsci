admin = "maureen"
name = str.lower(input("Enter your name: "))

while name != admin:
    name = str.lower(input("Access denied.\nEnter your name: "))

password = "watermelon"
pw = str(input("Welcome back Maureen! Please enter your password: "))

while pw != password:
    pw = str(input("Your password is incorrect. Passwords are case sensitive.\nPlease enter your password: "))

print("Access granted.")