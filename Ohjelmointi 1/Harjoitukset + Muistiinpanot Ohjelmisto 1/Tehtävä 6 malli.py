import random

N = n = 0

while N < 10 :
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    N += 1
    print("Arvottu piste: ")
        if x * x + y * y < 1 :
            n += 1
print(f"Pisteitä yhteensä {N}, joista ympyrän sisällä {n} ")
pi = 4 * n / N

    #TO DO laske piin likiarvo


