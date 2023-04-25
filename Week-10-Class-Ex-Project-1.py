#Jinny Choe
#4/24/2023
#Week 10 Class Exercise Project #1

class A: 
    def one (self):
        print("1")
    
    def two(self):
        print("2")

class B(A): #class B is inheriting from class A
    def three (self):
        print("3")

    def four (self):
        print("4")

#only sees objects in A
a1 = A()
a1.one()
a1.two()
a1.three()
a1.four()

#only sees objects in B
b1 = B()
b1.one()
b1.two()
b1.three()
b1.four()

