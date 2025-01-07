# Create student class that takes name and marks of 3 subjects as arguments in constructor.ConnectionResetError
# Then create a method to print the average
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def find_average(self):
        sum = 0
        for val in self.marks:
            sum = sum + val
        print("Hey" ,self.name,", " "Average of marks is ", sum/3)
            
        
s1 = Student("Shirish Baral",[99,98,97])
s1.find_average()

s1.name = "Not Shirish"
s1.find_average()


