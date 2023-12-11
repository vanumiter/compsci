number_list = []
for i in range(5):
    num = int(input("Enter a number: "))
    number_list.append(num)

for number in range(len(number_list)):
    number_list[number]+=1

print(("Modified list:", number_list))
    