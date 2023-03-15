#Jinny Choe
#3/13/2023 
#Week 5 Class Exercise Part#2 Project #2

#This program simulates 10 tosses of a coin
import random

#constants
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
    #simulate the coin toss
        if random.randint(HEADS,TAILS) == HEADS:
            print ("Heads")
        else:
            print("Tails")

#call main function
main()
 
  