import sys
import matplotlib.pyplot as plt
import numpy as np

print("This program models how compound interest affects money in common financial practices.")
print("It will cover three practices in particular:\n'Basic compound interest', 'Amortization', and 'Savings'.")
print("")
def basic(interest, present, years): # compound interest formula found in log tables
    return present*(1+(interest)/100)**years 
    
def mortgage(interest, present, months): # amortization formula, again found in log tables
     # prevents python from malfunctioning due to dividing by 0
    interest_monthly = ((1+(interest/100))**(1/12))-1 # converts APR from yearly to monthly
    return (present * interest_monthly * (1+interest_monthly) ** months) / (((1+interest_monthly) ** months) - 1)

def mortgage_total(interest, present, months): # amortization total, factoring in monthly interest
    interest_monthly = ((1+(interest/100))**(1/12))-1
    mortgage = (present * interest_monthly * (1+interest_monthly) ** months) / (((1+interest_monthly) ** months) - 1)
    return mortgage*months

def saving(interest, payment, months): # investment geometric sequence formula
    interest_monthly = (1 + interest / 100) ** (1 / 12) 
    total = (payment * interest_monthly * ((interest_monthly ** months) - 1)) / (interest_monthly - 1)
    return total

try: # prints message when user exits with ctrl + c
    choice = int(input("Choose which practice you would like to simulate by entering their respective numbers:\n1: Basic compound interest\n2: Amortization\n3: Savings\n\nEnter a number:\n"))

    while True:
        try: # loops until user enters valid inputs
            if choice == 1: # basic compound interest
                present = float(input("Enter the present value:\n"))
                interest = float(input("Enter the annual interest as a percentage:\n"))
                years = int(input("Enter the amount of years:\n"))

                x_years = np.arange(0., years + 1, 1)  # creating an array of years
                y_values = [basic(interest, present, eachyear) for eachyear in x_years]  # calculating values for each year

                print("€" + str(round(basic(interest,present,years), 2)) + " will be acculumated in total after " + str(years) + " years.")
                print("€" + str(round(basic(interest, present, years) - present, 2)) + " has been gained.")

                #acculumating value over time graph
                plt.plot(x_years, y_values)
                plt.xlabel('Years')
                plt.ylabel('€')
                plt.title('Value Over Time')
                plt.show()

                break

            elif choice == 2: # amortization
                present = float(input("Enter the amount of money to be loaned:\n"))
                interest = float(input("Enter the interest (APR) as a percentage:\n"))
                years = int(input("Enter the amount of years:\n"))

                mortgage = mortgage(interest, present, years*12)
                total = mortgage_total(interest, present, years*12)

                print("€" + str(np.round(mortgage, 2)) + " will be paid every month.")
                print("€" + str(np.round(total, 2)) + " will be paid in total after " + str(years) + " years.")
                print("You have paid an extra €" + str(round(total - present, 2)) + ".")

                x_years = np.arange(0., years + 1, 1)
                y_total_values = [mortgage*eachyear*12 for eachyear in x_years]

                # total paid over time graph
                plt.plot(x_years, y_total_values)
                plt.title("Total paid")
                plt.xlabel('Years')
                plt.ylabel('€')
                plt.show()
                break

            elif choice == 3: # investment
                payment = float(input("Enter the amount of money lodged into savings each month:\n"))
                interest = float(input("Enter the interest (AER) as a percentage:\n"))
                years = int(input("Enter the amount of years:\n"))

                print("€ " + str(round(saving(interest, payment, years*12), 2)) + " will be saved up after " + str(years) + " years.")
                print("You have earned €" + str(round(saving(interest, payment, years*12)-payment*years*12,2)) + ".")

                x_years = np.arange(0., years*12 + 1, 12)
                y_total_values = [saving(interest, payment, eachyear) for eachyear in x_years]

                # total money saved over time graph
                plt.plot(x_years, y_total_values)
                plt.title("Total money in savings account")
                plt.xlabel('Months')
                plt.ylabel('€')
                plt.show()
                break

            else:
                print("Invalid choice, exiting program.")
                sys.exit(0)


        except ValueError:
            print("Please enter a valid number.")
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit(0)

