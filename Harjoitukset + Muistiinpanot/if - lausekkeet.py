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