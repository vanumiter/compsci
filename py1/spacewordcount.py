inp = str(input("Enter any sentence: "))

count_space = 0
index = 0

space = ord(" ")

while index < len(inp):
    if ord(inp[index]) == space:
        count_space+=1
    else:
        pass    
    index+=1

print("Number of spaces:", count_space) 
print("Number of words:", count_space+1) # number of words in typical english sentence