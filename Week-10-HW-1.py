#Jinny Choe
#4/19/2023
#Week 10 Homework Project #1

class Pet:
    def __init__(self,name,species,age):
        self.__name = name
        self.__animal_type = species
        self.__age = age
        
    def set_name(self,name):
        self.__name = name
        return self.__name    
    
    def set_animal_type(self,species):
        self.__animal_type = species
        return self.__animal_type

    def set_age(self,age):
        self.__age = age
        return self.__age    

        


#start the main fxn
def main():
    name = (input("Enter the name of your pet: "))
    species = (input("Enter the type of your pet: "))
    age = (input("Enter the age of your pet: "))   
    
    myPet = Pet(name,species,age)
    
    v1 = myPet.set_name(name)
    v2 = myPet.set_species(species)
    v3 = myPet.set_age(age)

    print("Hello ",v1,", your address is ",v2,", ",v3," ",v4,". Your # is ",str(v5),". Your age is ",v6)

main()