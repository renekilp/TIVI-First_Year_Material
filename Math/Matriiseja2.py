import numpy as np

# Tehtävä 1. a) ja b)
A = np.array([[-1, 2], [3, 1]])
B = np.array([[0, 1, 3], [2, -3, 5]])
C = np.array([[1, 3, 5], [0, -2, 1], [2, -1, 4]])
D = np.array([[1], [-3], [-1]])

result1a = np.dot(A, B)
result1b = np.dot(C, D)

print("Tehtävä 1. a) ja b):")
print(result1a)
print("...ja b):")
print(result1b)

# Tehtävä 3.

A = np.array([[1, 2, 3], [1, 0, -2]])
B = np.array([[1], [4], [2]])
C = np.array([[1, 0, 2]])

resultAB = np.dot(A, B)
# resultBA = np.dot(B, A)  # Ei voi kertoa (B on 3x1 ja A on 2x3 - virhe!)
resultAC = np.dot(A, C.T)
# resultBC = np.dot(B, C)  # Ei voi kertoa (B on 3x1 ja C on 1x3 - virhe!)
resultCB = np.dot(C, B)

print("Tehtävä 3.")
print("A * B:")
print(resultAB)
# print(resultBA)  # Ei tulosta, koska virheellinen matriisikoko
print("A * C^T:")
print(resultAC)
print("C * A:")
# print(resultCA)   # Ei tulosta, koska virheellinen matriisikoko
# print(resultBC)  # Ei tulosta, koska virheellinen matriisikoko
print("C * B:")
print(resultCB)

# Tehtävä 5.
A = np.array([[-1, 0.5], [2, 1]])
B = np.array([[-1, -2], [2, 4]])

resultAB = np.dot(A, B)
resultBA = np.dot(B, A)

print("Tehtävä 5.")
print(resultAB)
print(resultBA)
