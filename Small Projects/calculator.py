import sys

def calculator():
    while True:
        print("Welcome to calculator \n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Multiplication")
        print("5. Exit")
        print("-----------------------------------")
        operator = int(input("Enter your choice: "))
    
        if operator == 5:
            print("Exiting...")
            sys.exit(0)
        
        num1 = int(input("Enter first number to operate: "))
        num2 = int(input("Enter second number to operate: "))
        
        result = calculate(operator, num1, num2)
        print("RESULT =", result)

def calculate(operator, a, b):
    if operator == 1:
        return a + b
    elif operator == 2:
        return a - b
    elif operator == 3:
        return a / b
    elif operator == 4:
        return a * b
    else:
        print("Invalid option!")
        return None


calculator()
