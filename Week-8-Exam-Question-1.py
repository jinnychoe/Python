#Jinny Choe
#4/10/2023
#Project 1

def userinput(): #gets user input for grams of fat and carbs
    while True:
        try: 
            fatgrams = float (input("How many grams of fat do you eat daily? "))
            carbgrams = float(input("How many grams of carbohydrates do you eat daily? "))
            return fatgrams, carbgrams #returns user input
        except ValueError: #if value is not a number, will again
            print("Please enter numerical values only")

def calc(fatgrams, carbgrams): #calculates calories from user input
    fatcal = fatgrams*9
    carbcal = carbgrams*4
    return fatcal, carbcal #returns calories of fat and carbs
    
def main():
    fatgrams, carbgrams = userinput()
    fatcal, carbcal = calc(fatgrams, carbgrams)
    fatcal = int(fatcal)
    carbcal = int(carbcal)
    print (f"The calories from fat intake: {fatcal:.2f}")
    print (f"The calories from carb intake: {carbcal:.2f}")

main()