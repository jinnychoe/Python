#Jinny Choe
#3/27/2023
#Week 7 Class Exercise Strings 5

#This program counts the number of times the letter T (uppercase or lowercase) appears in a string

def main():
    #create a variable to use to hold the count
    count = 0
    
    #get string from user
    my_string = input('Enter a sentence: ')
    
    #count the Ts
    for ch in my_string: 
        if ch == 'T' or ch == 't':
            count += 1
    
    #print the result.
    print(f'The letter T appears {count} times.')

#call the main function
if __name__ == '__main__':
    main()
