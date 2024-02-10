"""""

nimet = ['Aava', 'Bertil', 'Cecilia']
opnumero = [1243, 178236, 8912789]

opnumero[2]
opnumero['Aava']


k = {1: 333, 2: 453, 3: 224}

"""""

numerot = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}

numerot["Olga"] = "050-1011012"
numerot["Mary"] = "0401-2132139"

print (numerot)

nimi = input("Anna nimi: ")
if nimi in numerot:
    print (f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")

#   ----------------------------------------------

lukudict = {}   #   tee dictionary jossa avain = potenssiin 2

for i in range(1, 8):
    lukudict[i] = i ** 2
    print(lukudict)
