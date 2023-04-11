#Jinny Choe
#4/10/2023
#Project 4

expense_file_write = open("expenses.txt","a")
date = (input("What is the month and year: "))

while True:
    try:
        rent = float(input("Amount for rent: ")) #user input amount spent on rent
        break
    except ValueError:
        print("Invalid input. Numbers only...")
while True:
    try:
        gas = float(input("Amount for gas: ")) #user input amount spent on gas
        break
    except ValueError:
        print("Invalid input. Numbers only...")
while True:
    try:
        food = float(input("Amount for food: ")) #user input amount spent on food 
        break
    except ValueError:
        print("Invalid input. Numbers only...")
while True:
    try:
        clothes = float(input("Amount for clothing: "))#user input amount spent on clothes
        break
    except ValueError:
        print("Invalid input. Numbers only...")
while True:
    try:
        car = float(input("Amount for car payment: "))#user input amount spent on car payment
        break
    except ValueError:
        print("Invalid input. Numbers only...")
expense_file_write.write(f"{date}\nRent: ${rent:.2f}, Gas: ${gas:.2f}, Food ${food:.2f}, Clothes: ${clothes:.2f}, Car: ${car:.2f}") #writes to file
expense_file_write.close() #closes file
expense_file_read = open("expenses.txt","r") #opens file
print(expense_file_read.read()) #reads file and prints
expense_file_read.close() #closes file