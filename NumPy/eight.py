import numpy as np

# Searching in Array
np1 = np.array([1,2,3,4,5,3,7,8,3,10])
'''x = np.where(np1 == 3)
print(np1)
print(x[0])
print(np1[x[0]])
'''
# Return even items
y = np.where(np1 % 2 == 0)
print(np1)
print(y[0])
print(np1[y[0]])
