#Jinny Choe
#4/19/2023
#Week 9 Homework Project #3

class RetailItem: 
    def __init__(self,num,desc,units,price): #initialize attributes
        self.__num = num
        self.__desc = desc
        self.__units = units
        self.__price = price
    
    def set_num(self,num): #sets item number
        self.__num = num
        return self.__num
        
    def set_desc(self,desc): #sets description of item
        self.__desc = desc
        return self.__desc    

    def set_units(self,units): #sets number of units of item
        self.__units = units
        return self.__units    
    
    def set_price(self,price): #sets price of item
        self.__price = price
        return self.__price  
    
    def get_num(self): #gets number if item
        return self.__num
        
    def get_desc(self): #gets description of item
        return self.__desc

    def get_units(self): #gets number of units of item
        return self.__units

    def get_price(self): #gets price of item
        return self.__price
        
#start the main fxn
def main():

    item1 = RetailItem("1","Jacket","12","59.95") #creates instance of object
    item2 = RetailItem("2","Designer Jeans","40","34.95") #creates instance of object  
    item3 = RetailItem("3","Shirt","20","24.95") #creates instance of object
    
    RI1n = item1.get_num()#gets number of item
    RI1d = item1.get_desc() #gets description attribute
    RI1u = item1.get_units() #gets number of units attribute
    RI1p = item1.get_price()#gets price attribute

    RI2n = item2.get_num()#gets number of item    
    RI2d = item2.get_desc() #gets description attribute
    RI2u = item2.get_units() #gets number of units attribute
    RI2p = item2.get_price()#gets price attribute

    RI3n = item3.get_num()#gets number of item    
    RI3d = item3.get_desc() #gets description attribute
    RI3u = item3.get_units() #gets number of units attribute
    RI3p = item3.get_price()#gets price attribute
    
    print("\tDescription\tUnits in Inventory\tPrice")
    print(RI1n+"\t"+RI1d + "\t\t"+ RI1u+"\t\t\t"+RI1p)
    print(RI2n+"\t"+RI2d + "\t"+ RI2u+"\t\t\t"+RI2p)
    print(RI3n+"\t"+RI3d + "\t\t"+ RI3u+"\t\t\t"+RI3p)
    
main()
