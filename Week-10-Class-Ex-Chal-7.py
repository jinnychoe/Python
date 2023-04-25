#Jinny Choe
#4/25/2023
#Week 10 Class Exercise Challenge 7

class Employee:
    
    def __init__(self,name,number):#initialize var
        self.__name = name
        self.__number = number
        
    def set_name(self,name):   #mutator methods
        self.__name = name
        
    def set_number(self,number):
        self.__number = number
        
    def get_name(self):    #accessor methods
        return self.__name
        
    def get_number(self):
        return self.__number

class ProductionWorker(Employee): #subclass
    def __init__(self,name,number,shift,rate):
        super().__init__(name,number)
        self.__shift = shift
        self.__rate = rate
        
    def set_shift(self,shift): #mutator methods
        self.__shift = shift
    
    def set_rate(self,rate):
        self.__rate = rate
    
    def get_shift(self): #accessor methods
        if self.__shift == 1:
            return "Day"
        elif self.__shift == 2:
            return "Night"
        
    def get_rate(self):
        return self.__rate   
        
def main():
    name1 = input("Input the Production Worker name: ")
    number1 = int(input("Input the Production worker employee number: "))
    shift1 = int(input("Select 1 for day shift, 2 for night shift: "))
    rate1 = float(input("Input the Production worker hourly rate: "))
    
    worker1 = ProductionWorker(name1,number1,shift1,rate1) #create instance of object
    
    
    print("Name: ",worker1.get_name())
    print("ID number: ",worker1.get_number())
    print("Shift: ",worker1.get_shift())
    print("Hourly rate: ",worker1.get_rate())
    print("\n")
    
main()
        