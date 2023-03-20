#Jinny Choe
#3/20/2023
#Week 6 Class Exercise Project #3

def sales():
    num_days = int(input("Enter the days of sales: "))
    sales_file = open('sales.txt','a')
    
    for count in range(1, num_days+1): #start with 1, increment by 1
        #inside of loop because nested after the for loop
        try:
            sales = float(input("Enter the sales for day # "+str(count)+ ": "))        
        except ValueError:
            print("Invalid input, please enter a number.")
            return
        sales_file.write(str(sales)+'\n')
    
    #outside of the loop, by indenting
    sales_file.close()

def ReadSales(): #defines read fxn
    sales_file = open('sales.txt','r') #opens file to read
    
    line = sales_file.readline() #reads a line
    
    while line != '': #as long as empty string not returned
        
        try:
            amount = float(line)
        except ValueError:
            print("Invalid input in file, please check file contents.")
            return
        
        print(format(amount, '.2f')) #prints the line that was read
        line = sales_file.readline() #reads another line
    sales_file.close() #closes file

sales()
ReadSales()