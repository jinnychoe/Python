#Jinny Choe
#4/10/2023
#Project 2

coffee_file = open("Coffee.txt","r") #opens file to read

for line in coffee_file: #goes through each line in file
    print(line) #prints each line
    
coffee_file.close() #closes file
