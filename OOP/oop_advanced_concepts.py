# del: used to delete object properties or object itself
# del s1.name // del s1

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Shirish")
print(s1.name)
del s1.name
print(s1)
print(s1.name)


# Private; used for sensetive attribute, which we do not want is accessed outside of class

class Account:
    def __init__(self,acc_no,acc_pswd):
        self.acc_no = acc_no
        # self.acc_pswd = acc_pswd => Not private
        self.__acc_pswd = acc_pswd #Password can't be accessed outside of class

    def display_pswd(self):
        print(self.__acc_pswd)


shirish = Account("12345","abcde")
print(shirish.acc_no)
print(shirish.display_pswd())


# Here, private method __hello cannot be directly accessed but by a method within same class
'''
class Person:
    def __hello(self):
        print("Private method")

    def access(self):
        self.__hello()


a1 = Person()
a1.access()
'''

# Inheritance:
#When one class derives properties and methods of another class

class Car:
    color = "red"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Corrola")

print(car1.start())
print(car1.stop())
print(car2.color)














