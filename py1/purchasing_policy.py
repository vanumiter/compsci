price = int(input("Enter the price of the item: "))

if price > 10000:
    print("As the price is greater than €10,000, you must go to tender.")
elif price >= 500 and 10000 >= price:
    print("You must get quotes from three different suppliers.")
else:
    print("You are eligible to directly order the item.")