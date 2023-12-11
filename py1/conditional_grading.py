grade = int(input("Enter your grade as a percentage: "))

if grade > 100 or grade < 0:
    print("Please enter a valid grade.")
elif grade == 100 and grade > 89:
    print("Your result is a H1.")
elif 89 >= grade and grade > 79:
    print("Your result is a H2.")
elif 79 >= grade and grade > 69:
    print('Your result is a H3.')
elif 69 >= grade and grade > 59:
    print("Your result is a H4.")
else:
    print("lol")