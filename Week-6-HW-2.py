#Jinny Choe
#3/22/2023
#Week 6 Homework Question #2

def main():
    animal = input("Enter the name of an animal: ")
    fruit = input("Enter the name of a fruit: ")
    country = input("Enter the name of a country: ")
  
    file = open('things.txt','a') #opens file for append
    
    file.write(animal+ "\n" + fruit + "\n" + country + "\n") #writes to file
    
    file.close() #closes file
    
    readfile = open('things.txt','r') #opens file for read
    
    content = readfile.read() #reads file
    
    readfile.close() #closes file
    
    print(content) #prints file contents
    
    
main()