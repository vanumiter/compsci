hour_week = []
total_hours = 0

for i in range(7):
    hour = float(input(f"Enter hour value in day {i+1}: "))
    hour_week.append(hour)

for hours in hour_week:
    total_hours+=hours

# total milk price formula = total_hours*price*milk_per_hour

milk_price = float(input("Price of milk per litre: €"))
milk_per_hour = float(input("Average milk drank per hour in litres: "))
total_milk_price = total_hours*milk_price*milk_per_hour

print("The total price of the milk in one week is €" + str(round(total_milk_price, 2)))