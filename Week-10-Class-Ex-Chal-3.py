#Jinny Choe
#4/25/2023
#Week 10 Class Exercise Challenge 3

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

class car_demo(Automobiles): #inherits from automobiles
    def __init__(self,make,model,mileage,price):
        super().__init__(make,model,mileage,price)

def main():
    used_car = Automobiles("Audi",2022,45000,80000.0)
    print("Make: ",used_car.get_make())
    print("Model: ",used_car.get_model())
    print("Mileage: ",used_car.get_mileage())
    print("Price: ",used_car.get_price())
    print("\n")
    
    demo_car = car_demo("Honda",2022,45000,80000.0)
    print("Make: ",demo_car.get_make())
    print("Model: ",demo_car.get_model())
    print("Mileage: ",demo_car.get_mileage())
    print("Price: ",demo_car.get_price())

main()
        