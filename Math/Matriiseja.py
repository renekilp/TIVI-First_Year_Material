import numpy as np
import numpy.linalg as la

A = np.array([-1, 2, 3, -5])
B = np.array([2, 0, -1, 4])

#   Määritetään 2A + 3B

print(f"Tehtävän vastaus (2A + 3B):\n{2*A + 3*B}")

#   Ja lopuksi A - B

print(f"Tehtävän vastaus (A - B):\n{A - B}")


A = np.array([[5, 3, 0], [2, 1, 0]])
B = np.array([[-9], [4]])

X = la.inv(A).dot(B)

print(f"a) Vastaus:\n{X}")

A = np.array([[2, 1, 1], [1, 3, 1], [2, 1, 2]])
B = np.array([[6], [4], [9]])
X = la.inv(A).dot(B)

print(f"b) Vastaus:\n{X}")

A = np.array([[1, 1, 3], [3, 1, 1], [2, 1, 2]])
B = np.array([[-1], [5], [2]])
X = la.inv(A).dot(B)

print("Vastaus:\n Loputton / Ei vastausta") #  heittää errorin, koska loputon vastaus