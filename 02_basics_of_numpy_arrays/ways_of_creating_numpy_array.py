import numpy as np

a1 = np.array([1,2,3,4,5])
print(a1)

st = "Hello World"
a2 = np.fromiter(st, dtype = "U2")
print(a2)

a3 = np.arange(1,21,1)
print(a3)

a4 = np.linspace(1,21,3)
print(a4)

a5 = np.empty([2,3,4],dtype = "U2")
print(a5)

a6 = np.ones([2,3,4],dtype = "U2")
print(a6)

a7 = np.zeros([2,3,4],dtype = "f")
print(a7)