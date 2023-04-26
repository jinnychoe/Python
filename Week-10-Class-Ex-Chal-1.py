#Jinny Choe
#4/24/2023
#Week 10 Class Exercise Challenge 1

class AnimalType:
    def eats(self):
        print("This animal likes to eat?")
    
class rabbits(AnimalType):
    def munch(self):
        print(" carrots ")

class birds(rabbits):
    def munch1(self):
        print(" seeds ")
        
RabbitObject = rabbits()
RabbitObject.eats()
RabbitObject.munch()

BirdObject = AnimalType()
BirdObject = birds()

BirdObject.eats()
BirdObject.munch1()

RabbitBird = AnimalType()
RabbitBird = rabbits()
RabbitBird = birds()
RabbitBird.eats()
RabbitBird.munch()
RabbitBird.munch1()

