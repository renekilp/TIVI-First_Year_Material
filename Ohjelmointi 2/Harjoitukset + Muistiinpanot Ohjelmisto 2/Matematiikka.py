import numpy as np

#   tehtävä 1.1 s.8-9
#   a), b), c), d)

a = 2.493
b = 0.911
c = 137.7
d = 62.3

print(np.degrees(a))
print(np.degrees(b))
print(np.radians(c))
print(np.radians(d))

#   tehtävä 3

e = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for i in e:
  print(np.radians(e))

#   tehtävä 2.2.1 s.20

f = 1.6
g = 2.3

print(np.hypot(f, g))


