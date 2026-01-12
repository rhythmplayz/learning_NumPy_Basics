import numpy as np


#using np.array()
a1 = np.array([1,2,3])
a2 = np.array([[1,2],[2,3]])
a3 = np.array([[[1,2],[2,3]],[[3,4],[4,5]]])

print(a1)
print(a2)
print(a3)


#using numpy functions
b0 = np.zeros((10,5),dtype=np.int64)
b1 = np.ones((5,2))
br = np.arange(1,11,1)

print(b0)
print(b1)
print(br)