#Jinny Choe
#3/13/2023
#Week #5 Homework #5 Question #3

def totsales():
    totalsales = float(input("Please input the total sales for the month: $"))
    return totalsales
    
def countysalestax(totalsales):
    countytax = totalsales *0.025
    return countytax

def statesalestax(totalsales):
    statetax = totalsales*0.05
    return statetax

def totalsalestax(countytax, statetax):
    totaltax = countytax + statetax
    return totaltax
    
def main(): #defines main program
    totalsales = totsales()
    countytax = countysalestax(totalsales)
    statetax = statesalestax(totalsales)
    totaltax = totalsalestax(countytax, statetax)
    print (f"The total sales for the month is: ${totalsales:.2f}")
    print (f"The state sales tax for the month is: ${statetax:.2f}")
    print (f"The county sales tax for the month is: ${countytax:.2f}")
    print (f"The total sales tax for the month is: ${totaltax:.2f}")
    
main() #calls main