class Animal:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Animal: {self.name}"
    def __repr__(self):
        return self.__str__()
    
class Dog(Animal):
    def info(self):
        return f"Yo im a dog named {self.name}"
    def __str__(self):
        return f"Dog: {self.name}"
a1 = Animal("Lion")
print(a1)
d1 = Dog("Marshall")
print(d1)
print(d1.info())