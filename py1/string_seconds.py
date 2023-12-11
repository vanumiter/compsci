
hours = int(input("Enter the amount of hours: "))
minutes = int(input("Enter the amount of minutes: "))
seconds = int(input("Enter the amount of seconds: "))


hours = hours*60*60
minutes = minutes*60
total = hours+minutes+seconds

print("The total amount of time in seconds is", total)

