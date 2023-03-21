# Jinny Choe
# 3/21/2023
# Week 6 Class Exercise Challenge #7

def letter(grade): #determines letter grade
    if grade >= 90 and grade <=100:
        letter = "A"
    elif grade >=80 and grade <= 89:
        letter = "B"
    elif grade >=70 and grade <= 79:
        letter = "C"
    elif grade >= 60 and grade <= 69:
        letter = "D"
    else:
        letter = "F"
    return letter

def avg(midterm,final): #determines average grade
    average = 0
    average = (midterm+final)/2
    return average
    
def write(name,avg,letter): #writes name, average grade, letter grade into file
    text_file = open("Grades.txt", "a") #open text file to append
    content = text_file.write("\nName: " +name +". Average grade: "+str(avg)+", "+str(letter) +".")  #write in text file
    text_file.close() #close text file
    
def read(): #reads file
    text_file = open("Grades.txt","r")
    content = text_file.read()
    print(content)
    text_file.close()
    
def main():
    while True: 
        name = (input("Enter the full name: ")) #asks user for name
        try:
            if not name.strip():
                raise ValueError("Name cannot be empty.")
            break
        except ValueError as e:
            print(e)
            continue
        
    while True:   
        try:
            midterm_grade = float(input("Enter the numerical midterm grade: ")) #asks user for midterm grade
            finalexam_grade = float(input("Enter the numerical final exam grade: ")) #asks user for final exam grade
            break
        except ValueError:
            print ("Please enter numeric values for the grades.")
    
    avg_grade = avg(midterm_grade,finalexam_grade) #calls grade averaging fxn
    letter_grade = letter(avg_grade) #calls letter grade fxn
    file_write = write(name,avg_grade,letter_grade) #calls write fxn
    read() #calls read fxn
    
main()
