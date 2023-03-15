#Jinny Choe
#3/13/2023 
#Week 5 Class Exercise Part#1 Project #6

#The following is used as a global constant to represent the contribution rate
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Enter the gross pay: '))
    bonus = float(input('Enter the amount of bonuses: '))
    #calling the two functions
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)
    
#The show_pay_contrib function accepts the gross pay as an argument and displays the retirement contribution for the amount of pay.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print(f'Contribution for gross pay: ${contrib:,.2f}')
    
#The show_bonus_contrib function accepts the bonus amount as an argument and displays the retirement contribution for that amount of pay.

def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print(f'Contribution for bonuses: ${contrib:,.2f}.')

#call the main function
main()
    
