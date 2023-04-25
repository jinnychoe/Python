#Jinny Choe
#4/25/2023
#Week 10 Class Exercise Challenge 5

class Insect():
    
    def __init__(self,species): #initialize class
        self.__species = species

    def set_species(self,species):   #mutator methods
        self.__species = species
   
    def get_species(self):  #accessor methods
        return self.__species

class Bumblebee(Insect): #create subclass
    
    def __init__(self,species,sting,gender): #initialize subclass
        super().__init__(species)
        self.__sting = sting
        self.__gender = gender
        
    def set_sting(self, sting):     #mutator methods
        self.__sting = sting
        
    def set_gender(self, gender):
        self.__gender = gender
   
    def get_sting(self):   #accessor methods
        if self.__sting == "Y":
            return "has a stinger."
        elif self.__sting == "N":
            return "does not have a stinger."
    
    def get_gender(self):
        if self.__gender == "M":
            return "He"
        elif self.__gender == "F":
            return "She"
            
class Grasshopper(Insect): #create subclass
    
    def __init__(self,species,color,size): #initialize subclass
        super().__init__(species)
        self.__color = color
        self.__size = size
    
    def set_color(self,color):     #mutator methods
        self.__color = color
    
    def set_size(self,size):
        self.__size = size
    
    def get_color(self):   #accessor methods
        return self.__color
    
    def get_size(self):
        return self.__size    
        
def main():
    
    maya = Bumblebee("bumblebee","Y","F") #create instance of subclass
    hopper = Grasshopper("grasshopper","green","small")
    
    print("Maya is a "+maya.get_species()+". "+maya.get_gender()+" "+maya.get_sting())
    print("Hopper is a "+hopper.get_species()+" that is "+hopper.get_color()+" and "+hopper.get_size()+".")

    print("\n")
    
main()
        