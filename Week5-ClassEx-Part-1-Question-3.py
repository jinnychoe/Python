#Jinny Choe
#3/13/2023 
#Week 5 Class Exercise Part#1 Question#3

#create a global variable
number = 0


def main():
    global number
    num1 = int(input('Enter the first number: ')) #get user input
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))   
    show_number(num1,num2,num3)
    add(num1,num2,num3)
    print (f"The total is {total}")

#prints numbers
def show_number(num1,num2,num3): 
    print(f'The number you entered is {num1}, {num2}, {num3}.') 
    
#adds numbers    
def add(num1,num2,num3):
    global total
    total = num1+num2+num3
    return total
    
main()


