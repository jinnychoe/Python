#Jinny Choe
#4/10/2023
#Project 5

num = []
for n in range(20, 31):
    num.append(n)

total = sum(num) #calculates sum of all numbers

avg = total/len(num) #calculate average of all numbers

print(f"Sum: {total}")
print(f"Average: {avg:.2f}")