# class Dog:
#     def __init__(self,name,breed,colour):
#         self.name = name
#         self.breed = breed
#         self.colour = colour
#     def __str__(self):
#         return f"{self.name} is a {self.breed} with the coulour {self.colour}"
#     def bark(self,scared):
#         if scared:
#             return("woof")
#         else:
#             return("Bark!")
#     pass
# class Westie(Dog):
#     def __init__(self,name,breed,colour,needToPee):
#         super().__init__(name,breed,colour)
#         self.needToPee=True
#     def __str__(self):
#         if self.needToPee:
#             return f"{self.name} is the colour {self.colour} and needs to pee"
#         else:
#             return f"{self.name} is the colour {self.colour} and does not needs to pee"

# dog1=Westie("Marshall","Westie","White",True)
# dog2 = Dog("Freya","Westie","Brown")
# print(dog1)
# print(dog1.bark(True))
# print(dog2)
# print(dog2.bark(False))
from random import randrange
class Monsta:
    def __init__(self,name):
        self.name=name
        self.hp = 10
        self.dmg = randrange(1,10)

    def info(self):
        return f"{self.name}(HP:{self.hp}, DMG:{self.dmg})"
    def brainRot(self):
        if self.hp>9:
            pass
        elif self.hp ==9:
            self.hp +=1
        else:
            self.hp +=2
    def attack(self,other):
        other.hp = other.hp-self.dmg
zombie = Monsta("Greg")
mob2 = Monsta("Hawk Tuah Girl")
print(zombie.info())
print(mob2.info())
zombie.attack(mob2)
print(zombie.info())
print(mob2.info())