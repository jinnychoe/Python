#Jinny Choe
#4/19/2023
#Week 9 Homework Project #2

class Employee: 
    def __init__(self,name,IDnum,dept,title): #initialize attributes
        self.__name = name
        self.__IDnum = IDnum
        self.__dept = dept
        self.__title = title
        
    def set_name(self,name): #sets name
        self.__name = name
        return self.__name    

    def set_IDnum(self,IDnum): #sets ID number
        self.__IDnum = IDnum
        return self.__IDnum    
    
    def set_dept(self,dept): #sets department
        self.__dept = dept
        return self.__dept    

    def set_title(self,title): #sets title
        self.__title = title
        return self.__title        

    def get_name(self): #gets name
        return self.__name

    def get_IDnum(self): #gets ID number
        return self.__IDnum   

    def get_title(self): #gets title
        return self.__title

    def get_dept(self): #gets department
        return self.__dept
        
#start the main fxn
def main():

    Emp1 = Employee("Susan Meyers","47899","Accounting","Vice President") #creates instance of object
    Emp2 = Employee("Mark Jones","39119","IT","Programmer") #creates instance of object   
    Emp3 = Employee("Joy Rogers","81774","Manufacturing","Engineer") #creates instance of object    
    
    E1n = Emp1.get_name() #gets name attribute
    E1id = Emp1.get_IDnum() #gets ID number attribute
    E1t = Emp1.get_title()#gets title attribute
    E1d = Emp1.get_dept()#gets department attribute

    E2n = Emp2.get_name() #gets name attribute
    E2id = Emp2.get_IDnum() #gets ID number attribute
    E2t = Emp2.get_title()#gets title attribute
    E2d = Emp2.get_dept()#gets department attribute
    
    E3n = Emp3.get_name() #gets name attribute
    E3id = Emp3.get_IDnum() #gets ID number attribute
    E3t = Emp3.get_title()#gets title attribute
    E3d = Emp3.get_dept()#gets department attribute
    
    print("Name\t\tID number\tDepartment\tJob Title")
    print(E1n + "\t"+E1id+"\t\t"+E1t+"\t"+E1d)
    print(E2n + "\t"+E2id+"\t\t"+E2t+"\t"+E2d)
    print(E3n + "\t"+E3id+"\t\t"+E3t+"\t"+E3d)
main()
