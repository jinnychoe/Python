#Jinny Choe
#4/17/2023
#Week 9 Class Exercise Project #4

class Customer:
    def __init__(self,name,address,phone,age,city,zipcode):
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
        
    def set_age(self,age):
        self.__age = age
        return self.__age
        
    def set_zipcode(self,zipcode):
        self.__zipcode = zipcode
        return self.__zipcode
    
    def set_city(self,city):
        self.__city = city
        return self.__city

#start the main fxn
def main():
    name = (input("Enter the name "))
    address = (input("Enter the street address "))
    city = (input("Enter the city "))
    zipcode = (input("Enter the zipcode "))
    phone = (input("Enter the phone "))
    age = (input("Enter the age "))
    
    
    class7 = Customer(name, address, phone, age, city, zipcode)
    
    v1 = class7.set_name(name)
    v2 = class7.set_address(address)
    v3 = class7.set_city(city)
    v4 = class7.set_zipcode(zipcode)
    v5 = class7.set_phone(phone)
    v6 = class7.set_age(age)
    
    print("Hello ",v1,", your address is ",v2,", ",v3," ",v4,". Your # is ",str(v5),". Your age is ",v6)

main()