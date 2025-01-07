# Class is a blueprint for creating objects
# It defines the properties and methods of an object
'''
class Student:
    name = "shirish baral"
    age = 20

s1 = Student()
print(s1.name)
print(s1.age)
'''
   
# Constructor
# A special method in a class that is automatically called when an object is created from the class
# It is used to initialize the attributes of the class
'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student("shirish baral", 20)
print(s1.name)
print(s1.age)
'''


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year= year
s2 = Car("Mercedes","Benz-GLB","2025")
print(s2.brand)
print(s2.model)
print(s2.year)
        