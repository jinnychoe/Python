#Jinny Choe
#3/29/2023
#Week 7 Homework String #1
#Vowels, Consonants

def str_input():
    while True:
        user_input = input("Type in one word: ") #user input for a word
        if user_input.isalpha(): #checks if input is only alphabetical characters
            return user_input
        else: #if there are any non alpha characters ask for input again
            print("Type in only alpha characters!")
        
def count_vowels(string): #counts number of vowels
    count = 0 #intializes vowel counter
    for a in string: #checks each character in string to see if it is a vowel
        if a.lower() in "aeiou":
            count += 1 #if character is vowel, adds to vowel counter
    return count #returns count of vowels

def count_cons(string): #count number of consonants
    count = 0 #initializes consonant counter
    for a in string: #checks each character in string to see if it is consonant
        if a.lower() not in "aeiou": #of character is consonant, adds to consonant counter
            count += 1    
    return count #returns count of consonant

def main():
    an_input = str_input()
    num_vowels = count_vowels(an_input)
    num_cons = count_cons(an_input)
    print(f"The number of vowels: "+str(num_vowels))
    print(f"The numebr of consonants: "+str(num_cons))

main()
