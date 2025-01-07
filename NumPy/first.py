import numpy as np
list1 = np.array([1,2,3,4,99])
print(list1.shape)
print(list1)
print(np.arange(15))

# numbers from 50 to 100 in interval of 3
list3 = np.arange(50,100,3)
print(list3)

# Multidimensional zeros
list4 = np.zeros((2,10))
print(list4)

# Multidimensional full
list5 = np.full((3,10),7)
print(list5)
