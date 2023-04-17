#Jinny Choe
#4/17/2023
#Week 9 Class Exercise Project #2

class Teacher:
    #using init to create a customized constructor here we have 3 arguements
    def __init__(self,name,classRoom,course):
        self.name = name
        self.classRoom = classRoom
        self.course = course
    
    def GetProfessor(self):
        print("Professor Name is "+self.name)
        print("Professor assigned class is "+self.classRoom)
        print("Professor is teaching "+self.course)

#call 3 args
Teacher1 = Teacher ("Prof. Sim","A206","Python Programming")

Teacher1.GetProfessor()