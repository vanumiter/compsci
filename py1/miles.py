import time

miles = float(input("Enter the distance in miles here: "))

kilometres = int(round((miles*1.60935),0))

print("The distance in kilometres is", kilometres, "km.")
time.sleep(1)
print("Calculating price...")
time.sleep(2)

price = kilometres*900
#print(f"The price needed to fly {kilometres} km by helicopter is {price}.") python 3.6+
print("The price needed to fly", kilometres, "km by helicopter is €"+str(price)+".")