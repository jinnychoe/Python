#Jinny Choe
#3/20/2023
#Week 6 Class Exercise Project #4

def main():
    num_emps = int(input('Enter the number of employee records: ')) #user input for number of records
    
    emp_file = open ('employees.txt','w') #opens file to write
    
    for count in range (1, num_emps+1): #starts loop for number of records to input
        print ('Enter data for employee #', count)
        
        name = input("Name: ") 
        id_num = input("ID Number: ")
        dept = input ('Department: ')
        
        emp_file.write(name +'\n') #writes into file
        emp_file.write(id_num +'\n')
        emp_file.write(dept+'\n')
        
        print()
    
    emp_file.close()
    print('recorded'+'\n')
    
    read_empfile = open('employees.txt','r') #opens file to read
    
    line = read_empfile.readline() #reads a line
    n = 1    
    
    while line != '': #as long as empty string not returned
        
        #starts loop to read each line and print each line
        if n%3 == 1:
            print ("Name:",line, end='')
            n+=1
        elif n%3 == 2:
            print ("ID number:",line, end='')
            n+=1
        elif n%3 == 0:
            print ("Department:",line, end='')
            n+=1
            print('\n')
        line = read_empfile.readline() #reads next line
        
    read_empfile.close() #closes file
    
main()

