#Jinny Choe
#3/29/2023
#Week 7 Homework String #4
#Pig Latin

def str_input():
    while True:
        user_input = input("Type a sentence: ") #user input for a word
        return user_input

def tokenize(string):
    tokens = string.split(" ") #tokenize by spaces
    caps_words = [] #create new list
    for word in tokens:
        caps_words.append(word.upper()) 
    return caps_words
    
def piglatin(string):
    pig_translation_sentence = []
    for word in string:
        translated_word = word[1:]+word[0] + "AY"
        pig_translation_sentence.append(translated_word)
    return pig_translation_sentence
   
def main():
    an_input = str_input() #gets string from user
    string_token = tokenize(an_input)
    translation = piglatin(string_token)
    output_string = " ".join(translation)
   
    print(f"The output is {output_string}")

main()


