
height = int(input("Enter the height of the cylinder in centimetres here: "))
radius = int(input("Enter the radius of the cylinder in centimetres here: "))

pi = 3.14
volume = pi*(radius**2)*(height)

totalLiquid = int(input("Enter the amount of liquid in litres here: "))

cylinders = int(round((totalLiquid*1000)/volume, 0))

print("There are", cylinders, "cylinders required to hold", totalLiquid, "litres of liquid")
