#Jinny Choe
#3/29/2023
#Week 7 Homework String #2
#most freq char

def str_input():
    while True:
        user_input = input("Type in one word: ") #user input for a word
        if user_input.isalpha(): #checks if input is only alphabetical characters
            return user_input
        else: #if there are any non alpha characters ask for input again
            print("Type in only alpha characters!")

def counter(string): #fxn counts letters in string
    character_count = {} #intializes an empty dictionary
    for character in string: #goes through each letter in string
        if character in character_count: #if letter already exists in dictionary, adds to counter
            character_count[character] += 1
        else: #puts the letter in the dictionary
            character_count[character] = 1
    return character_count
    


def main():
    an_input = str_input() #gets string from user
    character_count = counter(an_input) #create dictionary for each letter in string
    most_common_character = max(character_count, key=character_count.get) #gets most common letter in string by finding which character has highest count
    print(f"The most common letter in '{an_input}' is '{most_common_character}'. There are {character_count[most_common_character]} of '{most_common_character}' ")
   

main()
