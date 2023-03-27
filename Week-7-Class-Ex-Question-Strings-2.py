#Jinny Choe
#3/27/2023
#Week 7 Class Exercise Strings 2

#The get_login_name function accepts a first name, last name, and ID number as arguments. It returns a system login name

def get_login_name(first, last, idnumber):
    #get the first three letters of the first name
    #if the name is less than 3 characters, the slice will return the entire first name
    set1 = first[0:3]
    
    #get the first three letters of the last name.
    #if the name is less than 3 characters, the slice will return the entire last name
    set2 = last[0:3]
    
    #get the last three characters of the student ID
    #if the ID num is less than 3 characters, the slice will return the entire ID num
    set3 = idnumber[-3:]
    
    #put the sets of characters together.
    login_name = set1 + set2 + set3
    
    #return the login name
    return login_name

#The valid_password function accepts a password as an argument and returns either true or false to indicate whether the password is valid.
#a valid password must be at least 7 characters in length, have at least one uppercase letter, one lowercase letter and one digit.

def valid_password(password):
    #set the boolean variables to false
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    is_valid = False

    #begin the validation
    #start by testing the password's length
    
    if len(password) >= 7:
        correct_length = True
    
        #Test each character and set the appropriate flag when a required character is found
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
        
        #determine whether all the requirements are met
        #if they are, set is_valid to true
        #otherwise, set is_valid to false
        if correct_length and has_uppercase and has_lowercase and has_digit:
            is_valid = True
        else: 
            is_valid = False
    
    #return the is_valid variable
    return is_valid
    
    #this program gets a password from the user and validates it
    


def main():
    #get password from user
    password = input('Enter your password: ')
        
    #validate the password
    while not valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')
        
    print('That is a valid password')

#call main fxn
if __name__=='__main__':
    main()
