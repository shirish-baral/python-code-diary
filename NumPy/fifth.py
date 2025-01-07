import numpy as np

# Create 1-D Numpy array
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(np1)
print(np1.shape)

np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
# print(np2)
print(np2.shape)
# Reshape 2-D
np3 = np1.reshape(3,4)
print(np3)

# FLatten 1-D
np4 = np3.reshape(-1)
print(np4)



