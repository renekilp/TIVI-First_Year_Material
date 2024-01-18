katkoviiva = "-"
print(katkoviiva * 80 + "\n Minun nimeni on René." + "\n" + katkoviiva * 80)

#   -----------------------------------------------------

luku = 3
print("Minä asun osoitteessa " + str(luku))
print(f"Minä asun osoitteessa {luku}")

#   -----------------------------------------------------

sentti = 2.54

user_input = input("Syötä pituus tuumana: \n")
user_int = int(user_input)
new_value = sentti * user_int
print("Pituus senttimetreinä: \n" + str(new_value) + " cm")

#   -----------------------------------------------------

#   5f, 10.2f, <20s, 8d

#   import math / esim print(math.pi) / from math import pi
import math
munpi = math.pi
print(f'{munpi:10.5f}') #   10 (meinaa riviä). 5(meinaa desimaalia)f

luku = 10
print(f"{luku: 10d}") # 10 rivi

#   -----------------------------------------------------


#rahat = float(input("Anna rahamäärä: "))


#   -----------------------------------------------------

luku = 11

if luku < 9:
    print("hello")
print("moi")
