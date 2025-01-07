'''
Define a Circle class to create a circle with radius r using constructor
Define an Area() method of the class which calculates area of circle
Define a Perimeter() method of class which allows you to calcuate the perimeter of circle

class Cricle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def permieter(self):
        return 2 * (22/7) * self.radius

c1 = Cricle(21)
print(c1.area())
print(c1.permieter())
'''

'''
Define a Employee class with attributes role, department and salary.
This class has a showDetails() method.
Create an Engineer class that inherits properties from Employee and has
attributes: name & age
'''
class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role is ",self.role)
        print("Department is ",self.department)
        print("Salary is ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age= age
        super().__init__("Engineer","Software","1,00,000")


eng1 = Engineer("Shirish Hero",20)
eng1.showDetails()







