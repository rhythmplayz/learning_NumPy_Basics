import numpy as np

dtype = [("name", "S10"),("year", int),("cgpa", float)]

vals = [("a",2003,4.0),
        ("c",2001,3.9),
        ("b",2003,3.1),
        ("d",2002,2.0),
        ("e",2005,3.0), ]

a = np.array(vals, dtype=dtype)

print(a)

print(np.sort(a))
print(np.sort(a, order= "name"))
print(np.sort(a, order = ["year", "cgpa"]))