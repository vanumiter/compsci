num = int(input("Enter a number: "))
index = 0
total = num

while index < 6:
    num = int(input("Enter another number: "))
    index+=1
    total+=num
    print("The sum of the current numbers is", total)

print("The final sum of the numbers is", total)
print("The average of the numbers provided to 3 decimal places is", round(total/6, 3))

