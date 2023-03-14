#Jinny Choe
#3/13/2023
#Week #5 Homework #5 Question #1

def actual_value(): #gets user input for actual value of property
    actvalue = float(input("Input the actual value of the property: $"))
    return actvalue
    
def assess_value(actvalue): #calculates assessed value at 60% of actual value
    assessedvalue = actvalue*0.6
    return assessedvalue
    
def prop_tax(assessedvalue): #calculates property tax at 72cents per 1dollar
    proptax = assessedvalue*.72
    return proptax

def main(): #defines main program
    actvalue = actual_value()
    assessedvalue = assess_value(actvalue)
    proptax = prop_tax(assessedvalue)
    print (f"The actual value of the property is ${actvalue:.2f}")
    print (f"The assessed value of the property is ${assessedvalue:.2f}")
    print (f"The property tax of the property is ${proptax:.2f}")
    
main() #calls main