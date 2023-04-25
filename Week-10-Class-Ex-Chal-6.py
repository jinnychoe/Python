#Jinny Choe
#4/25/2023
#Week 10 Class Exercise Challenge 6
class Automobiles:
    
    def __init__(self,make,model,mileage,price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
 
    #mutator methods
    def set_make(self,make):
        self.__make = make
    
    def set_make(self,model):
        self.__model = model
    
    def set_mileage(self,mileage):
        self.__mileage = mileage
    
    def set_price(self,price):
        self.__price = price
    
    #accessor methods
    def get_make(self):
        return self.__make
        
    def get_model(self):
        return self.__model
    
    def get_mileage(self):
        return self.__mileage
    
    def get_price(self):
        return self.__price
        
    def get_doors(self):
        return self.__doors

class Truck(Automobiles): #inherits from automobiles
    def __init__(self,make,model,mileage,price):
        super().__init__(make,model,mileage,price)
        
class SUV(Automobiles): #inherits from automobiles
    def __init__(self,make,model,mileage,price):
        super().__init__(make,model,mileage,price)
 
class EV(Automobiles): #inherits from automobiles
    def __init__(self,make,model,mileage,price):
        super().__init__(make,model,mileage,price)
        
def main():
    used_car = Automobiles("Audi",2022,45000,80000.0)
    print("Make: ",used_car.get_make())
    print("Model: ",used_car.get_model())
    print("Mileage: ",used_car.get_mileage())
    print("Price: ",used_car.get_price())
    print("\n")
    
    used_car1 = Automobiles("Honda",2022,45000,80000.0)
    print("Make: ",used_car1.get_make())
    print("Model: ",used_car1.get_model())
    print("Mileage: ",used_car1.get_mileage())
    print("Price: ",used_car1.get_price())
    print("\n")

    truck = Truck("Toyota","Tacoma",40000,12000.0)
    suv = SUV("Volvo","SE",30000,18500.0)
    
    print("The following truck is in inventory")
    print("Make: ",truck.get_make())
    print("Model: ",truck.get_model())
    print("Mileage: ",truck.get_mileage())
    print("Price: ",truck.get_price())
    print("\n")

    print("The following SUV is in inventory")
    print("Make: ",suv.get_make())
    print("Model: ",suv.get_model())
    print("Mileage: ",suv.get_mileage())
    print("Price: ",suv.get_price())
    print("\n")
    ev = EV("Polestar","2",30000,18500.0)
    
    print("The following EV is in inventory")
    print("Make: ",ev.get_make())
    print("Model: ",ev.get_model())
    print("Mileage: ",ev.get_mileage())
    print("Price: ",ev.get_price())

main()
        