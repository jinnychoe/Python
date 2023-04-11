#Jinny Choe
#4/10/2023
#Project 6

num = []
for n in range(20, 31):
    num.append(n)

total = sum(num) #calculates sum of all numbers

avg = total/len(num) #calculate average of all numbers

for n in num: #finds the number 27
    if n == 27:
        print (f"The list contains {n}")
