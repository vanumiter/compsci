import time
garden_length = int(input("Give the length of the garden in metres here: "))
garden_width = int(input("Give the width of the garden in metres here: "))
house_length = int(input("Give the length of the house in metres here: "))
house_width = int(input("Give the width of the house in metres here: "))

garden_area = garden_length*garden_width
house_area = house_length*house_width
area = garden_area-house_area

print("The area of your garden excluding the house situated inside it is", area, "metres squared.")
time.sleep(3)

rate = int(input("Give how much square metres of grass will be cut per second. "))

time = round((area/rate)/60, 2)

print("It will take", time, "minutes to cut", area, "square metres of grass.")
