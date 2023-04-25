#Jinny Choe
#4/25/2023
#Week 10 Class Exercise Challenge 2

#initialize person class
class person:
    def __init__(self,name,age,address,city,state,zipcode):
        self.name = name
        self.age = age 
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

#the student class is inheriting from the person class
class Student(person):
    def __init__(self,name,age,address,city,state,zipcode,studentID,GPA):
        #the super keyword is calling the super class which is the person person class and passing name, age
        super().__init__(name,age,address,city,state,zipcode)
        self.studentID=studentID
        self.GPA=GPA

#teacher class inheriting from person class
class Teacher(person):
    def __init__(self,name,age,address,city,state,zipcode,TeacherID,ClassTeaching):
        super().__init__(name,age,address,city,state,zipcode)
        self.TeacherID = TeacherID
        self.ClassTeaching = ClassTeaching

#get user input for student
student_name = input("Enter student name: ")
student_age = input("Enter student age: ")
studentID = input("Enter student ID: ")
GPA = input("Enter GPA: ")
student_address = input("Enter the street address: ")
student_city = input("Enter the city: ")
student_state = input("Enter the state: ")
student_zipcode = input("Enter the zipcode: ")

#create instance of student
student = Student(student_name,student_age,student_address,student_city,student_state,student_zipcode,studentID, GPA)

#get user input for teacher
teacher_name = input("Enter teacher name: ")
teacher_age = input("Enter teacher age: ")
teacherID = input("Enter teacher ID: ")
ClassTeaching = input("Enter name of course taught: ")
teacher_address = input("Enter the street address: ")
teacher_city = input("Enter the city: ")
teacher_state = input("Enter the state: ")
teacher_zipcode = input("Enter the zipcode: ")

#create instance of teacher
teacher = Teacher(teacher_name,teacher_age,teacher_address,teacher_city,teacher_state,teacher_zipcode,teacherID,ClassTeaching)

#print student instance
print("Student Name: ",student.name)
print("Student Age: ",student.age)
print("Student ID: ",student.studentID)
print("Student GPA: ",student.GPA)
print("Student Address: ",student.address,",",student.city,",",student.state,student.zipcode)

#print teacher instance
print("Teacher name: ", teacher.name)
print("Teacher Age: ",teacher.age)
print("Teacher ID: ",teacher.TeacherID)
print("Teacher Course: ",teacher.ClassTeaching)
print("Teacher Address: ",teacher.address,",",teacher.city,",",teacher.state,teacher.zipcode)
