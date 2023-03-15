#Jinny Choe
#3/13/2023 
#Week 5 Class Exercise Part #2 Question #2

#gets user input for different costs
def costs():
    loan = float(input("Input the monthly loan payment: "))
    ins = float(input("Input the monthly insurance costs: "))
    gas = float(input("Input the monthly gas costs: "))
    oil = float(input("Input the monthly oil change costs: "))
    tire = float(input("Input the monthly tire costs: "))
    maint = float(input("Input the monthly maintenance costs: "))

    return loan, ins, gas, oil, tire, maint

#calculates total costs with arguments from user input
def calc(loan, ins, gas, oil, tire, maint):
    totalmonthly = loan+ins+gas+oil+tire+maint
    totalannual = 12*totalmonthly
    print (f"The total monthly costs are ${totalmonthly:.2f}")
    print (f"The total annual costs are ${totalannual:.2f}")
   
#defines main fxn
def main():
    loan, ins, gas, oil, tire, maint = costs()
    calc(loan, ins, gas, oil, tire, maint)
    
#calls main
main()
