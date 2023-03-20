#Jinny Choe
#3/20/2023
#Week 6 Class Exercise Challenge #2

def WriteNumbers(): #defines write input fxn
    outfile = open('numbers.txt','a') #appends to file
    
    num1 = int(input('enter #1: ')) #user input
    num2 = int(input('enter #2: '))
    num3 = int(input('enter #3: '))
    
    sum = num1+num2+num3 #calculates sum
    avg = sum/3 #calculates average
    
    outfile.write("The 1st number is " + str(num1) + '\n') #writes to file
    outfile.write("The 2nd number is " + str(num2) + '\n')
    outfile.write("The 3rd number is " + str(num3) + '\n')
    outfile.write("The avg number is " + str(avg) + '\n')
    outfile.write("The sum number is " + str(sum) + '\n')
    
    print("Data recorded.")

WriteNumbers() #runs fxn

def ReadNumbers(): #defines read fxn
    
    infile = open('numbers.txt','r') #opens file to read
    readfile = infile.read() #reads file
    print(readfile) #prints contents from file it read

ReadNumbers() #runs rxn