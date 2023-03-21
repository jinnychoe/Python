#Jinny Choe
#3/20/2023
#Week 6 Class Exercise Project #4

def main():
    num_emps = int(input('Enter the number of employee records: '))
    
    emp_file = open ('employees.txt','w')
    
    for count in range (1, num_emps+1):
        print ('Enter data for employee #', count)
        
        name = input("Name: ")
        id_num = input("ID Number: ")
        dept = input ('Department: ')
        
        emp_file.write(name +'\n')
        emp_file.write(id_num +'\n')
        emp_file.write(dept+'\n')
        
        print()
    
    emp_file.close()
    print('recorded')

main()