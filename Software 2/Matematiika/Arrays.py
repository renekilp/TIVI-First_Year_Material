import numpy as np
from numpy import linalg

x = np.array([2, 2])
y = np.array([4, 1])
a = np.random.randint(20, size=(4, 5))

sorted_array = np.sort(a, axis=None)
reshaped_array = sorted_array.reshape(a.shape)
print(f"Array with random integers: \n{reshaped_array}")

u = np.array([2, 3])
v = np.array([4, -7])

uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])

vectors = [("u", u), ("v", v), ("uu", uu), ("vv", vv)]

for name, vector in vectors:
    print(f"{name}: {vector} ")

for i in range(4):
    name, vector = vectors[i]
    print(f"Norm of {name}: {linalg.norm(vector, axis=None)}")