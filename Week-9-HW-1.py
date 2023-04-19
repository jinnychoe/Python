#Jinny Choe
#4/19/2023
#Week 9 Homework Project #1

class Pet: 
    def __init__(self,name,species,age): #initialize attributes
        self.__name = name
        self.__animal_type = species
        self.__age = age
        
    def set_name(self,name): #sets name
        self.__name = name
        return self.__name    
    
    def set_animal_type(self,species): #sets animal type
        self.__animal_type = species
        return self.__animal_type

    def set_age(self,age): #sets age
        self.__age = age
        return self.__age    

    def get_name(self,name): #gets name
        return self.__name
    
    def get_animal_type(self,species): #gets animal type
        return self.__animal_type
    
    def get_age(self,age): #gets age
        return self.__age


#start the main fxn
def main():
    name = (input("Enter the name of your pet: ")) #user input for name
    species = (input("Enter the type of your pet: ")) #user input for type
    age = (input("Enter the age of your pet: "))    #user input for age
    
    myPet = Pet(name,species,age) #creates instance 
    
    P1 = myPet.get_name(name) #gets instance name
    P2 = myPet.get_animal_type(species) #gets instance type
    P3 = myPet.get_age(age)#gets instance age

    print("Hello "+P1+". You are a "+P2+" that is "+P3+" years old.")

main()
