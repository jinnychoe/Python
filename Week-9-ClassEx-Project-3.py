#Jinny Choe
#4/17/2023
#Week 9 Class Exercise Project #3

class PI:
    #pass 3 parameters
    def GetInformation(self,LN,FN,Age):
        return LN + ", " + FN + ", " + str(Age)

PersonalInformation = PI()
PersonalInformation.Lastname = input("Enter the last name ")
PersonalInformation.Firstname = input("Enter the first name ")
PersonalInformation.Age = int(input("Enter the age "))

print(PersonalInformation.GetInformation(PersonalInformation.Lastname,PersonalInformation.Firstname,PersonalInformation.Age))
