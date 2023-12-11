rain_week = []
total_rain = 0
outlier_length = []
outlier_day = []


for i in range(7):
    rain = float(input(f"Enter the rainfall (cm) measured in day {i+1}: "))
    rain_week.append(rain)
    
    if rain > 3.5:
        outlier_length.append(rain)
        outlier_day.append(i+1)

    total_rain += rain

# average rainfall = total_rain / 7

print("The total rainfall for this week is", total_rain, "cm.")
print("The average rainfall for this week is", round(total_rain/7,2), "cm per day.")

# [0:-1] gets all of the elements of the list except the last element, which is called separately in the later print function. 
# str[1:-1] converts the table into a string, allowing the index to exclude the square brackets.
string_outlier_length = str(outlier_length[0:-1])[1:-1]
string_outlier_day = str(outlier_day[0:-1])[1:-1]


if len(outlier_length) != 0: # runs code if outlier list isn't empty
    if len(outlier_length) > 1:
        print(f"On days {string_outlier_day} and {outlier_day[-1]}, the rainfall exceeded 3.5 cm.")
        print(f"The rainfall on each day respectively were {string_outlier_length} and {outlier_length[-1]} cm.")
    else:
        print(f"On day {outlier_day[0]}, the rainfall exceeded 3.5 cm.")
        print(f"The rainfall on that day was {outlier_length[0]} cm.")
