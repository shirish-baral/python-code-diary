import numpy as np

# Slicing Numpy Arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])

# Return 2,3,4,5
print(np1[1:5])

# Return from something till end
print(np1[1:])

# Return 7,8
print(np1[-3:-1])

# Steps
print(np1[1:5])
print(np1[1:9:2])

# Steps on entire array
print(np1[::3])

# Slice 2-d array
np2 = np.array(
    [[1,2,3,4,5], [6,7,8,9,10]])
# Pull ou a single item
print(np2[1,3])

 


