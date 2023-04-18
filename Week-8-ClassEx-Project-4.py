#Jinny Choe
#4/17/2023
#Week 9 Class Exercise Project #4

class Customer:
    def __init__(self,name,address,phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    
    def set_name(self,name):
        self.__name = name
        return self.__name
    
    def set_address(self,address):
        self.__address = address
        return self.__address
        
    def set_phone(self,phone):
        self.__phone = phone
        return self.__phone

#start the main fxn
def main():
    name = (input("Enter the name "))
    address = (input("Enter the address "))
    phone = (input("Enter the phone "))
    
    class7 = Customer(name,address,phone)
    
    v1 = class7.set_name(name)
    v2 = class7.set_address(address)
    v3 = class7.set_phone(phone)
    
    print("Hello ",v1,", your address is ",v2,"and your # is ",str(v3))

main()
