#Jinny Choe
#3/13/2023 
#Week 5 Class Exercise Part #1 Project #3

#This program demonstrates two functions that have local variables with the same name

def main():
    #call texas function
    texas()
    #call california function
    california()
    
#definition of the texas function. it creates a local variable named birds
def texas():
    birds = 5000
    print(f'texas has {birds} birds.')

#definition of california function. It also creates a local variable named birds
def california():
    birds = 8000
    print(f'california has {birds} birds.')
    
#call the main function
main()
