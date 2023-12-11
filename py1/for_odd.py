value = int(input("Enter a value: "))

# prints out odd numbers from 1 to value (value+1 used in case the value was an odd number, which would not be printed out if the extra step wasn't included) 
for odd in range(1, value+1, 2):
        print(odd)

