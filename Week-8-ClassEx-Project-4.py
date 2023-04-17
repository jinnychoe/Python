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
    
    def set_address(self,address):
        self.__address = address
        
    def set_phone(self,phone):
        self.__phone = phone

#import the other class file name
import class7

#start the main fxn
def main():
    name = (input("Enter the name "))
    address = (input("Enter the address "))
    phone = (input("Enter the phone "))
    
    #call class7 or the first file then the name of the class, then the name of the fxn which equals to the input var
    
    v1 = class7.Customer.set_name = name
    v2 = class7.Customer.net_address = address
    v3 = class7.Customer.set_phone = phone
    
    print("Hello "+v1+", your address is "+v2+"and your # is "+v3)

main()