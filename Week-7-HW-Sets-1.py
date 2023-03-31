#Jinny Choe
#3/27/2023
#Week 7 Homework Set Question #1

#This program uses a dictionary as a deck of cards.
import random

def main():
    #create a deck of cards.
    deck = create_deck()

    #initialize hands of each player
    hand1 = 0 
    hand2 = 0
    
    #deal the cards until one hand is > 21
    while hand1 <= 21 and hand2 <= 21:
        hand_value1 = deal_cards(deck, 1, "Player 1")
        hand1 += hand_value1
        print("Player 1 has", hand1)
        hand_value2 = deal_cards(deck, 1, "Player 2")
        hand2 += hand_value2
        print("Player 2 has", hand2)
    
    #who is the winner
    if hand1 > 21 and hand2 > 21:
        print ("Both players have lost.")
    elif hand1 > 21:
        print("Player 2 wins!")
    elif hand2 > 21:
        print("Player 1 wins!")
    elif hand1 > hand2:
        print("Player 1 wins!")
    elif hand2 > hand1:
        print("Player 2 wins!")
    else:
        print("Player 1 and Player 2 are tied.")
    
#create_deck fxn returns a tuple representing a shuffled deck of cards
def create_deck():  #create a tuple with each card and its value stored as key-value pairs.
 
    deck = [('Ace of Spades', 1), ('2 of Spades', 2), ('3 of Spades', 3), ('4 of Spades', 4), ('5 of Spades', 5),
            ('6 of Spades', 6), ('7 of Spades', 7), ('8 of Spades', 8), ('9 of Spades', 9), ('10 of Spades', 10),
            ('Jack of Spades', 10), ('Queen of Spades', 10), ('King of Spades', 10),
            ('Ace of Hearts', 1), ('2 of Hearts', 2), ('3 of Hearts', 3), ('4 of Hearts', 4), ('5 of Hearts', 5),
            ('6 of Hearts', 6), ('7 of Hearts', 7), ('8 of Hearts', 8), ('9 of Hearts', 9), ('10 of Hearts', 10),
            ('Jack of Hearts', 10), ('Queen of Hearts', 10), ('King of Hearts', 10),
            ('Ace of Clubs', 1), ('2 of Clubs', 2), ('3 of Clubs', 3), ('4 of Clubs', 4), ('5 of Clubs', 5),
            ('6 of Clubs', 6), ('7 of Clubs', 7), ('8 of Clubs', 8), ('9 of Clubs', 9), ('10 of Clubs', 10),
            ('Jack of Clubs', 10), ('Queen of Clubs', 10), ('King of Clubs', 10),
            ('Ace of Diamonds', 1), ('2 of Diamonds', 2), ('3 of Diamonds', 3), ('4 of Diamonds', 4), ('5 of Diamonds', 5),
            ('6 of Diamonds', 6), ('7 of Diamonds', 7), ('8 of Diamonds', 8), ('9 of Diamonds', 9), ('10 of Diamonds', 10),
            ('Jack of Diamonds', 10), ('Queen of Diamonds', 10), ('King of Diamonds', 10)]
    
    #shuffles the deck
    random.shuffle(deck)
    
    #return the deck
    return deck
    
def deal_cards(deck,number,player_name):
    #initializes an accumulator for the hand value
    hand_value = 0
    
    #make sure the number of cards dealt is not greater than the number of cards in the deck
    if number > len(deck):
        number = len(deck)
        
    #deal the cards and accumulate their values
    for count in range(number):
        card = deck.pop()
        print(f"{player_name} has: {card[0]}")

    #determines value of Ace card
        if card[0].startswith('Ace'):
            ace_value = int(input("Do you want the ace value to be 11 or 1? "))
            while ace_value != 1 and ace_value != 11:
                ace_value = int(input("Invalid input. Select 11 or 1: "))
            if hand_value + ace_value > 21:
                hand_value += ace_value
        else:
            hand_value+=card[1]
    
    return hand_value
    
#call the main fxn
if __name__ == '__main__':
    main()
        
        