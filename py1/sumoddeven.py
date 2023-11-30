limit = int(input("Enter a number greater than 0: "))

num_odd = -1
num_even = 0

iteration = 0

total_odd = 0
total_even = 0

while iteration < limit:
    
    num_odd+=2
    total_odd+=num_odd

    if total_even < limit:
        num_even+=2
        total_even+=num_even
    else:
        pass
    
    iteration+=2

print("total odd", total_odd)
print("total even", total_even)