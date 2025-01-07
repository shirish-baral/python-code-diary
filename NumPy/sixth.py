import numpy as np

# 1-D
'''
np1 = np.array([1,2,3,4,5,6,7,8,9,10])
for x in np1:
     print(x)
'''
'''
# 2-D
np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for x in np2:
    # print rows print(x)
    for y in x:
        print(y)
'''
# 3-D
np3 = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
# for x in np3:
#    for y in x:
#        for z in y:
#            print(z)

# Use np.nditer()
for x in np.nditer(np3):
    print(x)