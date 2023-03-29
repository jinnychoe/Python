#Jinny Choe
#3/29/2023
#Week 7 Homework String #3
#Word Separator

def str_input():
    while True:
        user_input = input("Type a sentence: ") #user input for a word
        return user_input

def tokenize(string):
    tokens = string.split(" ") #tokenize by spaces
    capitalized_words = [] #create new list
    for word in tokens:
        capitalized_words.append(word.capitalize())  #capitalize first letter of the word

    return capitalized_words
   
def main():
    an_input = str_input() #gets string from user
    string_token = tokenize(an_input)
    output_string = "".join(string_token)
   
    print(f"The output is {output_string}")

main()

