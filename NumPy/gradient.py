import numpy as np
def f(x):
    return x**2
def df(x):
    return 2*x
def gradient_descent(learning_rate, initial_x, num_iterations):
    x = initial_x
    for i in range(num_iterations):
        gradient = df(x)
        x = x - learning_rate * gradient
        print(f"Iteration {i+1}: x = {x}, f(x) = {f(x)}")
    return x

learning_rate = 0.1
initial_x = 10
num_iterations = 20
min_x = gradient_descent(learning_rate, initial_x, num_iterations)
print(f"Minimum value of x found: {min_x}")