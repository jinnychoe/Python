#Jinny Choe
#3/13/2023 
#Week 5 Class Exercise Part#1 Project #5

#create a global variable

number = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_number()
    
def show_number():
        print(f'The number you entered is {number}.')

main()

def add(num1,num2):
    global total
    total = num1+num2
    return total
    
a=add (3,4)
print (a)