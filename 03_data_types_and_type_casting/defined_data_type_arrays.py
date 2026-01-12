import numpy as np

a1 = np.zeros([2,3,4],dtype = "f")
print(a1.dtype)
a2 = np.zeros([2,3,4],dtype = np.complex128)
print(a2.dtype)
a3 = np.zeros([2,3,4],dtype = np.int64)
print(a3.dtype)
a4 = np.zeros([2,3,4],dtype = np.float64)
print(a4.dtype)