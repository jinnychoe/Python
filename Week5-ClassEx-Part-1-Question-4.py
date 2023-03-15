#Jinny Choe
#3/13/2023 
#Week 5 Class Exercise Part#1 Question #4

#create a global variable

number = 0

def main():
    global number
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))   
    show_number(num1,num2,num3)
    add(num1,num2,num3)
    avg(num1,num2,num3)
    print (f"The total is {total}")
  
    print (f"The average is {avg:.1f}")
    
def show_number(num1,num2,num3):
    print(f'The number you entered is {num1}, {num2}, {num3}.')
    
def add(num1,num2,num3):
    global total
    total = num1+num2+num3
    return total

def avg (num1,num2,num3):
    global avg
    avg = (total/3)
    return avg
 
main()