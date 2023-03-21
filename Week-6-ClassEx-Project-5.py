# Jinny Choe
# 3/20/2023
# Week 6 Class Exercise Project #5

def main():
    while True:
        try: #try the batch of code below, if there are no errors than disregard the except
            hours = int(input('Hours worked: '))
            pay = float(input('Hourly pay: '))
            gross = hours * pay
            print('gross pay $', format(gross,',.2f'))
            break
            print('recorded')
        
        except ValueError: #if there are errors on the try statement, run the below print
            print ('Error: hours worked and pay must be valid numbers, try again')
        
        except Exception as err: #built-in Exception error processing
            print (err)
main()
