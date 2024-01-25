import random

N = n = 0

while N < 10 :
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    N += 1
    print(f"Arvottu piste: {x,y}\n")
    if x * x + y * y < 1 :
        n += 1

pi = 4 * n / N
print(f"Pisteitä yhteensä {N}, joista ympyrän sisällä {n}")
print(f"Piin liki arvo on:\n{pi}")