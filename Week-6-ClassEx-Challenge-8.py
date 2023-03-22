# Jinny Choe
# 3/21/2023
# Week 6 Class Exercise Challenge #8
import random

def random_generator(): #random num generator fxn
    r = random.randint(1,10) #generates random num
    return r #returns random number
    
def write(num): #write fxn
    text_file = open("Randoms.txt", "a") #open text file to append
    content = text_file.write(str(num)+ "\n")  #write in text file
    text_file.close() #close text file
    
def read(): #read file fxn
    text_file = open("Randoms.txt","r") #opens file
    content = text_file.read() #reads file
    print(content) #prints from file
    text_file.close() #close file
    
def main():
    while True: 
        value = (input("The number of random values that you want: ")) #asks user value
        try:
            if not value.strip():
                raise ValueError("Name cannot be empty.") #error if value is empty
            value = int(value)
            break
        except ValueError as e:
            print(e)
            continue
    
    for i in range(value):
        random_num = random_generator() #calls random num generator fxn
        write_num = write(random_num) #calls write fxn
    
    read_num = read()
    
main()

