rahat = (float(input("Rahat: ")))
if rahat >= 5:
    print("Voin ostaa latte")
else:
    print("VITUN KÖYHÄ!")

#   ------------------------------------

a = False
b = False
c = True

d1 = (a and b) or c # sulut ensin
d2 = a and (b or c) # sulut ensin
d3 = a and b or c   # and ensin, sitten or

print(d1)
print(d2)
print(d3)

#   -----------------------------------
ikä = int(input("Anna ikä: "))
if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg):"))
if (ikä >= 18 or (ikä >=15 and paino >= 55)):
    print("Lääkkeen käyttö sallittu!")
else: print("Lääkkeen käyttö ei sallittu!")

#   -------------------------------------
"""
import random

dice = random.randint(0, 1)
if dice == 0:
    print("Sinulle syntyi tyttö 😎 .")
else: print("Sinulle syntyi poika 😊 .")

"""
#   while - silmukat (loopit)


#jakolasku

num1 = float(input("Anna jaettava: "))
num2 = float(input("Anna jakaja: "))
while num2 == 0: #  muuta if = while (looppaa eikä jätä kesken)
    print("Jakaja ei olla nolla!")
    num2 = float(input("Anna uusi jakaja: "))

result = num1 / num2
print(f"Tulos: {result}")

# iteraatio (käytetään "laskuria" silmukoiden toistokertojen määrittelyyn)

#   i käytetään yleensä juuri "laskurin" nimeämisessä 'iteraattori'
#i = 1
i = int(input('Mistä numerosta aloitetaan:\n'))
amount = int(input("Kuinka monta numeroa tulostetaan:\n"))
offset = int(input("Anna numeroiden väli:\n"))
max_number = amount * offset + i
while i < max_number:
    print(f"Numero on {i}")
    i = i + offset
print(f"i:n lopullinen arvo silmukan jälkeen: {i}")
