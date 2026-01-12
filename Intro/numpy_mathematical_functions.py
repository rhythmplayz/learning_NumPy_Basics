import numpy as np

a = np.array([0,1,2,3,4,5])
print(np.exp(a))
print("0th index gives inf  | rest ",np.log(a[1:]))
print("0th index gives inf  | rest ",np.log10(a[1:]))
print(np.power(a,2))
print(np.square(a))
print(np.absolute(a))
print(np.sqrt(a))

b = np.array([np.pi,np.pi/2,np.pi/4,np.pi/8,0])
print(np.sin(b))