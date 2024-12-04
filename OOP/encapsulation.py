from typing import Any


class Person:
    def __init__(self,name,wealth):
        self.name = name
        self.__wealth = wealth # encapsulated(only accessable in the class)

    @property# @ is a decorator on a function. @property allows a method to act as an attribute
    def wealth(self):
        return self.__wealth
    
    @wealth.setter
    def wealth(self,new_value):
        self.__wealth = new_value

    def info(self):
        return f"Person(Name:{self.name}, Wealth:{self.__wealth})"
    
p1 = Person("Mr. Park", 69)
p2 = Person("Marshall", 100000)
p1.name = "Lebron James"
p1.wealth = "broke"
print(p1.wealth)
# p1.wealth = 69000000
# print(p1.info())