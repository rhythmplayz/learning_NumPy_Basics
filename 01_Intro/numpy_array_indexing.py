import numpy as np


#indexing
#  1  2  3  4  5  elements
#  0  1  2  3  4  positive indexing
# -5 -4 -3 -2 -1  negative indexing
a1 = np.array([10,20,30,40,50])

print(a1[2])
print(a1[-1])

a2 = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(a2[0,2])