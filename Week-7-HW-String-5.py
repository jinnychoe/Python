#Jinny Choe
#3/29/2023
#Week 7 Homework String #5
#Caesar Cipher

def str_input(): #fxn to get user input
    while True: 
        user_input = input("Type a sentence: ") #user input for a word
        return user_input

def tokenize(string): #fxn to tokenize string
    tokens = string.split(" ") #tokenize by spaces
    token_list = [] #create new list
    for word in tokens:
        token_list.append(word) #adds tokenized words to list
    return token_list #returns list
    
def cipher(string):
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #defines alphabet
    alphabet_shift_13 = alphabet[13:]+alphabet[:13] #defines shifted alphabet
    caesar_string='' #initializes final ciphered string
    for letter in string.upper(): #loops through each letter in string
        if letter in alphabet: 
            index = alphabet.index(letter) #finds index of letter in regular alphabet
            caesar_string += alphabet_shift_13[index] #finds letter in shifted alphabet by index
        else: 
            caesar_string += letter #if char is a space, just adds the space to the ciphered string
    return caesar_string 
    
def main():
    an_input = str_input() #gets string from user
    string_token = tokenize(an_input) #tokenizes string
    shifted_words = [cipher(word) for word in string_token] #sends each word in list to be ciphered
    output_string = " ".join(shifted_words) #prints ciphered string
   
    print(f"The output is {output_string}")

main()