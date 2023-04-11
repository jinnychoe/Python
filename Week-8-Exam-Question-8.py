#Jinny Choe
#4/10/23
#Week 8 Exam Question 8

name_list = []

while True:
    try: #asks user how many names to input
        num_names = int(input("How many names do you want to input? ")) 
        break
    except ValueError: #throws error if not whole number
        print("Invalid input. Enter a whole number only.")

for i in range(num_names): #write names to list
    while True:
        name = input(f"Enter name #{i+1}: ")
        if name.strip() != "":#checks if name is blank
            break
        else:#throws error if no name
            print("Name cannot be blank. Please try again.")
    name_list.append(name)
    
print("Names: ")
for name in name_list:#prints names in list
    print(name)




