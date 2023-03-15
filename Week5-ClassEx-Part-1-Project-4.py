#Jinny Choe
#3/13/2023 
#Week 5 Class Exercise Part #1 Project #4

#This program demonstrates passing two string arguemnts to a function
def main():
    first_name = input ('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is ')
    reverse_name(first_name, last_name)
    
def reverse_name(first,last):
    print (last, first)

#call main function
main()
