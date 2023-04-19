#Jinny Choe
#4/17/2023
#Week 9 Class Exercise Project #5

class BankAccount:
    def __init__(self,bal):#self used to represent instance of class, used to access var that bleong to class
    
        self.__balance = bal
    
    def deposit (self,amount):
        #add balance
        self.__balance += amount
    
    def withdraw(self,amount):
        if self.__balance >=amount:

            #subtract the balance
            self.__balance-=amount

        else:
            print ('Error: insufficient funds.')
    
    def get_balance(self):
        return self.__balance


#start the main fxn
def main():
    start_bal=float(input("Enter the starting balance "))
    
    savings = BankAccount(start_bal)
    
    pay = float(input("How much were you paid this week? "))
    print ("Will deposit that amount into your account")
    
    savings.deposit(pay)
    
    print("Your account balance is $ ",format(savings.get_balance(),',.2f'))
    
    cash = float(input ("How much would you like to withdraw? "))
    print ("Will withdraw that amount from your account")
    
    savings.withdraw(cash)

    print("Your account balance is $",format(savings.get_balance(),',.2f'))

main()
