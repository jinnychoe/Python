#Jinny Choe
#3/20/2023
#Week 6 Class Exercise Challenge #1

#this program writes to a file
def WriteInput(): #This function will allow user to write the input

    firstname = input("Input the first name: ")
    lastname = input("Input the last name: ")
    age = input("Input the age: ")
    
    file = open('file.txt', 'a') #appends input to file
    
    file.write ("Name: "+firstname +" "+ lastname + '\n') #writes input to file
    file.write ("Age: " + age+'\n')

    file.close() #closes file
    print('Information recorded.')
    
WriteInput() #runs write input function

def read():
    infile = open('file.txt','r') #opens file to read
  
    fileContents = infile.read() #reads file

    infile.close() #closes file

    print(fileContents) #prints file contents 

read() #runs read function
