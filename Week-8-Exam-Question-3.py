#Jinny Choe
#4/10/2023
#Project 3


brand = input ("Enter your favorite coffee brand: ") #user input brand name

prodnum = (input("Enter the product number: ")) #user input product number

while True:
    try:
        price = float(input("Enter the price: "))#user input price
        break
    except ValueError:#if not number, asks for numbers only
        print("Invalid input. Only numerical numbers")

coffee_file = open("Coffee.txt", "a")
coffee_file.write(f"{brand},{prodnum},{price:.2f}\n")

coffee_file = open("Coffee.txt","r") #opens file to read

for line in coffee_file: #goes through each line in file
    print(line) #prints each line

coffee_file.close() #closes file
