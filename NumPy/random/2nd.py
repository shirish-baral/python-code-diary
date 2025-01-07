import numpy as np
from numpy import random
'''
# 2-D array with 3 rows, each containing 5 random integers from 0 to 100
x = random.randint(100, size=(3,5))
print(x)

# Generate 1-D array with 5 random floats
y = random.rand(5)
print(y)

# Gnerate 2-D arway with 3 rows, each containinf 5 random elements
y1 = random.rand(3,5)
print(y1)

# Random number from an array
ele = random.choice([3,5,7,9,100])
print(ele)
'''
# 2-D array that consists of values in array parameter (3,5,7 and 9)
ele1 = random.choice([3,5,7,9], size=(3,5))
print(ele1)


