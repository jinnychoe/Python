#Jinny Choe
#3/13/2023 
#Week 5 Class Exercise Part#2 Project #3

import random

while True:
    user = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock","paper","scissors"]
    computer = random.choice(possible_actions)
    print(f"\nYou chose {user}, computer chose {computer}.\n")
    
    if user == computer:
        print(f"Both payers selected {user}. It's a tie!")
    elif user == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print ("Paper covers rock! You lose.")
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if computer == "paper":
            print ("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    
    play_again = input ("Play again? y/n: ")
    if play_again.lower() != "y":
        break