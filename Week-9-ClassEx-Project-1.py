#Jinny Choe
#4/17/2023
#Week 9 Class Exercise Project #1

class Students:
    #the keyword (self) is used to access variables that belong to the class
    def GetInformation(self):
        print("Student last name is " + self.Lastname)
        print("Student first name is " + self.Firstname)
        print("Student address is " + self.Address)
        print("Student city is " + self.City)
        print("Student State is "+ self.State)
        print("Student Zipcode is "+ self.Zipcode)
        
#creates the Student1 object
Student1 = Students()
Student1.Lastname = "Doe"
Student1.Firstname = "Jane"
Student1.Address = "111 St"
Student1. City = "Santa Ana"
Student1.State = "CA"
Student1.Zipcode = "12345\n"

#creates Student2 object
Student2 = Students()
Student2.Lastname = "Cantor"
Student2.Firstname = "Mike"
Student2.Address = "222 St"
Student2. City = "Garden Grove"
Student2.State = "CA"
Student2.Zipcode = "67890\n"

#call fxn
Student1.GetInformation()
Student2.GetInformation()
