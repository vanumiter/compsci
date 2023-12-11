fish = int(input("Enter the portions of fish: "))
chips = int(input("Enter the portions of chips: "))

price_fish = 4.5
price_chips = 2.8
vat = 0.09

calc = round((fish*price_fish)+(chips*price_chips), 2)
calc_vat = round(calc*vat, 2)

print("The total amount due excluding VAT is €" + str(calc))
print("The VAT that should be charged on the total amount is €" + str(calc_vat))