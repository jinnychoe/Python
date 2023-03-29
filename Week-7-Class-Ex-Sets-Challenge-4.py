#Jinny Choe
#3/27/2023
#Week 7 Class Exercise Sets Dictionaries Challenge #4

#this program will ask for the week sales to get the total and store it in a list

def main():
    days_in_the_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    week_sales = []
    
    print('Enter the sales for the week. \n')
    
    index = 0
    for i in days_in_the_week:
        sales = float(input(f'Enter the sales for {i}: '))
        week_sales.insert(index, sales)
        index += 1
    
    total_sales = total(week_sales)
    print(f'Thetoal sales of the week is ${total_sales:,.2f}')
    
    write('week_sales.text',week_sales, total_sales)
    
def total(number):
    sum = 0 
    for value in number:
        sum += float(value or 0)
    return sum

def write (name, sales, total):
    output = open(name, 'w')
    for money in sales:
        output.writelines(str(money)+'\n')
    output.writelines(f'Total sales: ${total:,.2f}')
    output.close()

main()
