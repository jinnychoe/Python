# Jinny Choe
# 3/20/2023
# Week 6 Class Exercise Challenge #3

def sales():
    num_days = int(input("Enter the number of days of sales: "))
    sales_file = open('sales.txt', 'a')
    
    for day_number in range(1, num_days+1):
        sales = float(input("Enter the sales for day #" + str(day_number) + ": "))
        sales_file.write(str(sales) + '\n')
        
    sales_file.close()

def read_sales():
    total_sales = 0
    sales_file = open('sales.txt', 'r')
    line = sales_file.readline()
    day_number = 1
    
    while line != '':
        amount = float(line)
        print("Sales for day #" + str(day_number) + ": " + format(amount, '.2f'))
        total_sales += amount
        day_number += 1
        line = sales_file.readline()
        
    sales_file.close()
    return total_sales

def salary():
    base_salary = float(input("Enter the base salary: "))
    total_sales = read_sales()
    
    if total_sales > 1000:
        commission = total_sales * 0.1
        salary = base_salary + commission
    else:
        salary = base_salary
        
    print("Total sales: " + format(total_sales, '.2f'))
    print("Salary: " + format(salary, '.2f'))

sales()
salary()