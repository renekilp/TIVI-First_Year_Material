import numpy as np

    #   tehtävä 1

teht_list = [2.493, 0.911]  #   rad
teht2_list = [137.7, 62.3]  #   degrees

print("Muunnetaan radiaaneiksi:")
for i in teht_list:
    print(f"{np.degrees(i):.2f} rad")

    #   tehtävä 2

print("\nMuunnetaan asteiksi:")
for i in teht2_list:
    print(f"{np.radians(i):.2f}°")

    # tehtävä 3

teht3_list = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360] #   degrees

print("\nMuodostetaan taulukko:")
for i in teht3_list:
    print(f"{i}° = {np.radians(i):.2f} rad")

    # tehtävä 4

a = 1.6     # m
b = 2.3     # m

print(f"\nSuorakulmaisen kolmion sivut: {a} m ja {b} m \nLasketaan hypotenuusa:\n{np.hypot(a, b):.2f} m")



