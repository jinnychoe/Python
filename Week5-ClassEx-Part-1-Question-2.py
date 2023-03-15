#Jinny Choe
#3/13/2023 
#Week 5 Class Exercise Part #1 Question #2

def firstname():#asks for first name
    global firstname
    firstname = input("Enter your first name: ")

def lastname():#asks for last name
    global lastname
    lastname = input("Enter your last name: ")

def address():#asks for address
    global address
    address = input("Enter your street address: ")

def city():#asks for city
    global city
    city = input("Enter your city: ")

def state():#asks for state
    global state
    state = input("Enter your state: ")

def zipcode():#asks for zipcode
    global zipcode
    zipcode = input("Enter your zipcode: ")

def main(): #define main function
    firstname()
    lastname()
    address()
    city()
    state()
    zipcode()
    print ("Your first name is: ",firstname)
    print ("Your last name is: ",lastname)
    print ("Your address is: ",address)
    print ("Your city is: ",city)
    print ("Your state is: ",state)
    print ("Your zipcode is: ",zipcode)
    
main()#call main
