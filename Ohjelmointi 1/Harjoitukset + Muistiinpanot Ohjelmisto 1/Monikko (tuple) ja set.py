"""
# Muistuttaa listaa, mutta käytetään silloin kun lista on pysyvä eikä muutu!
# esim. viikonpäivät, [1-7]

munmunikko = (1, 3, 5,) # 0, 1 , 2, 4, 5, 6 #   sulkuja ei välttämättä tarvitse mutta yleensä laitetaan
#   print(munmunikko[1:5:2]) # alku, loppu, step
eka, toka, kolmas = munmunikko
print(toka)

"""
"""
lista = ["John", 1, 5, 3, 1, True, "John", "John"]
lista2 = []

for i in lista:
    if i not in lista2 or type(i) == bool:
        lista2.append(i)

print(lista2)

#   -------------------------------------

#   joukku 'set'

pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

pelit.add("Cluedo")
print(pelit)

for p in pelit:
    print(p)

"""""
#   ------------------------------------

nimet = ["John", 1, 5, 3, 1, "John", 1]
nimet2 = set()

for name in nimet:
    if name not in nimet2:
        nimet2.add(name)

# to do muuta listaksi

print(nimet2)