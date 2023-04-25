#Jinny Choe
#4/25/2023
#Week 10 HW Project 2

class Person():
    def __init__(self,name,address,phone):
        self.__name=name
        self.__address=address
        self.__phone=phone
    
    def set_name(self,name):
        self.__name = name
    def set_address(self,address):
        self.__address=address
    def set_phone(self,phone):
        self.__phone
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone

class Customer(Person):
    def __init__(self,name,address,phone,ID,mail):
        super().__init__(name,address,phone)
        self.__ID = ID
        self.__mail = mail
    
    def set_ID (self,ID):
        self.__ID = ID
    
    def set_mail(self,mail):
        self.__mail = mail
    
    def get_ID(self):
        return self.__ID
    
    def get_mail(self):
        if self.__mail == True:
            return ("Yes")
        elif self.__mail == False:
            return ("No")

def main():
    customer1 = Customer("Jinny","123 Chapman Ave","714-123-4567","1234",True ) 
    print("Customer name:",customer1.get_name())
    print("Address:",customer1.get_address())
    print("Phone:",customer1.get_phone())
    print("ID number:",customer1.get_ID())
    print("On mailing list?",customer1.get_mail())
    print("\n")
    
main()
        