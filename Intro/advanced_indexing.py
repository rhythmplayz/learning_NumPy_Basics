import numpy as np

a = np.array([10,20,30,40,50,60])

# indexing using a array of index numbers
idx = np.array([1,3,5])
print(a[idx])

# indexing using a condition
condition = a > 20
print(a[condition])