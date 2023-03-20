#Jinny Choe
#3/20/2023
#Week 6 Class Exercise Project #2

def WriteNumbers():
    outfile = open('numbers.txt','a')
    
    num1 = int(input('enter #1: '))
    num2 = int(input('enter #2: '))
    num3 = int(input('enter #3: '))
    
    sum = num1+num2+num3
    avg = sum/3
    
    outfile.write("The 1st number is " + str(num1) + '\n')
    outfile.write("The 2nd number is " + str(num2) + '\n')
    outfile.write("The 3rd number is " + str(num3) + '\n')
    outfile.write("The avg number is " + str(avg) + '\n')
    outfile.write("The sum number is " + str(sum) + '\n')
    
    print("Data recorded.")

WriteNumbers()