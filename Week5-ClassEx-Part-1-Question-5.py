#Jinny Choe
#3/13/2023 
#Week 5 Class Exercise Part#1 Question #5

#asks for user input for total hours worked
def time():
    global time
    time = float (input("Enter the number of hours worked: "))
    return time
   
#asks for user input for hourly wage    
def hourlypay():
    global hourlypay
    hourlypay = float(input("Enter the hourly pay: "))
    return hourlypay

   #calculates total pay
def salary (time,hourlypay):
    global salary
    salary = time * hourlypay
    return salary

   #characterizes main function
def main():
    time()
    hourlypay()
    salary(time,hourlypay)
    print(f"Total hours worked: {time} hours")
    print(f"Hourly wage: ${hourlypay:.2f}")
    print(f"Total pay: ${salary:.2f}")

    #calls main fxn
main()
