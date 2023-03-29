#Jinny Choe
#3/29/2023
#Week 7 Homework String #1
#Vowels, Consonants

def str_input():
    while True:
        user_input = input("Type in one word: ") #user input for a word
        if user_input.isalpha():
            return user_input
        else: #if there are any non alpha characters ask for input again
            print("Type in only alpha characters!")
        
def count_vowels(string):
    count = 0
    for a in string:
        if a.lower() in "aeiou":
            count += 1
        #count number of vowels
    return count

def count_cons(string):
    count = 0
    for a in string:
        if a.lower() not in "aeiou":
            count += 1 
        #count number of consonants
    return count

def main():
    an_input = str_input()
    num_vowels = count_vowels(an_input)
    num_cons = count_cons(an_input)
    print(f"The number of vowels: "+str(num_vowels))
    print(f"The numebr of consonants: "+str(num_cons))

main()