#Jinny Choe
#4/17/2023
#Week 9 Class Exercise Challenge #3

class PI:
    #pass 3 parameters
    def GetInformation(self,LN,FN,Age,Add,City,State,Zip):
        return LN + ", " + FN + ", " + str(Age) + "\n" + Add + "\n" + City + ", " +State +" " + Zip
        
PersonalInformation = PI()
PersonalInformation.Lastname = input("Enter the last name ")
PersonalInformation.Firstname = input("Enter the first name ")
PersonalInformation.Age = int(input("Enter the age "))
PersonalInformation.Address = input("Enter the address ")
PersonalInformation.City = input("Enter the city ")
PersonalInformation.State = input("Enter the state ")
PersonalInformation.Zip = input("Enter the zip code ")

print(PersonalInformation.GetInformation(PersonalInformation.Lastname,PersonalInformation.Firstname,PersonalInformation.Age,PersonalInformation.Address,PersonalInformation.State,PersonalInformation.City,PersonalInformation.Zip))
