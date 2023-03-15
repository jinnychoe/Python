#Jinny Choe
#3/13/2023 
#Week 5 Class Exercise Part #2 Question #1

#converts kilometers to meters
def convert(km):
    mile = km*0.6214
    return mile


def main(): 
    distance = float(input("Input the distance in kilometers: ")) #user input for distance
    mile = convert(distance) #calls convert fxn
    print(f"The distance in miles: {mile:.1f}") #prints mile conversion

    #calls main fxn
main()
