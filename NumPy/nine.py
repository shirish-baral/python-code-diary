import numpy as np

# Filtering Numpy Arrays with Boolean Index Lists
np1 = np.array([1,2,3,4,5,6,7,8,9,10])
'''
filtered = []
for thing in np1:
    if thing % 2 ==0:
        filtered.append(True)
    else:
        filtered.append(False)

print(np1)
print(filtered)
print(f"Even Numbers are {np1[filtered]}")

# Shortcut
filtered = np1 > 5
print(np1)
print(filtered)
print(np1[filtered])
'''
arr = np.array([1, 2, 3, 4], ndmin =2)
print(arr)