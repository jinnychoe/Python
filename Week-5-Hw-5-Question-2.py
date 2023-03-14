#Jinny Choe
#3/13/2023
#Week #5 Homework #5 Question #2

def classA (): #asks user for total number of A seats
    seats = int(input("Input the total number of seats sold for Class A seats: "))
    classAtotal = seats * 20 #calculates income from seats
    return classAtotal 
    
def classB (): #asks user for total number of B seats
    seats = int(input("Input the total number of seats sold for Class B seats: "))
    classBtotal = seats * 15 #calculates income from seats
    return classBtotal
    
def classC (): #asks user for total number of C seats
    seats = int(input("Input the total number of seats sold for Class C seats: "))
    classCtotal = seats * 10 #calculates income from seats
    return classCtotal

def sumtot(a,b,c): #calculates sum from all seat sales
    total = a+b+c
    return total
    
def main(): #defines main program
   a = classA()
   b = classB()
   c = classC()
   total = sumtot(a,b,c)
   print (f"The total income generated from ticket sales is: ${total:.2f}")
   
main() #calls main