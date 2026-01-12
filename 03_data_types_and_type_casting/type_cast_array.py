import numpy as np

a1 = np.array([1,2,3,4,5], dtype = np.int64)
print(a1)
print(a1.dtype)

a2 = a1.astype(np.float64)
print(a2)
print(a2.dtype)