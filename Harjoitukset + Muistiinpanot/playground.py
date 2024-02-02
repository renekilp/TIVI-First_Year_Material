"""""
import random

dice = random.randint(1,6)
print(f"Arvottu numero:\n{dice}")

#   -------------------------------------------

player_count = 6
dice_amount = 1

best_player = None
best_result = 0

#   jokainen pelaaja suorittaa vuorollaan
current_player = 1
while current_player <= player_count:
    result = 0 # silmälukujen summa ennen noppien heittoa
    throw_count = 0 # iteraattori nopan heitoille (laskuri)
    # noppia heitettään dice_amount muuttujassa annettu määrä
    while throw_count < dice_amount:
        die = random.randint(1,6)
        print(f"Pelaaja {current_player}, {throw_count}. Heitto {die}")
        result = result + die
        throw_count += 1 # sama kuin throw_count = throw_count + 1
    print(f"Pelaajan {current_player} tulos: {result}")
    # testataan saatiinko uusi paras tulos, ja tallennetaan tarvittaessa edelliseen
    # parhaan tuloksen tulijalle,  päivitetään samalla paras pelaaja
    if result > best_result:
        best_result = result
        best_player = f"Pelaaja {current_player}"
    # jos tulos ei ole parempi, mutta on sama kuin edellinen tulos,
    # lisätään tai yhdistetään pelaajan nimi
    elif result == best_result:
        best_player = best_player + f", Pelaaja: {current_player}"

    current_player = current_player + 1
print(f"Paras tulos: {best_result} ja  {best_player}")


#   break komento heittää ylos aktiivisesta silmukasta. suoritus jatkuu koodilohkon jälkeen

counter = 0

while True: #   ikuinen silmukka
    print(f"laskuri eka {counter}")
    counter += 1
    if counter == 5:
        break # poistuu silmukan koodilohkosta samantien. alla oleva ei tulostu
    print(f"Laskuri toka {counter}")


probabilities = [0.52, 0.49, 0.72, 0.81, 0.12, 0.11]
prob_list = []

for prob in probabilities:
    if prob > 0.5:
        prob_list.append(1)
    if prob < 0.5:
        prob_list.append(0)
print(f'{prob_list}')



lista = [1, 2, 3, 5]
lista2 = [4, [6, 8], 9]
lista.extend(lista2)

print(lista[5][1])


"""""
def lasku(m_gallona):
    while m_gallona >= 0:
        litroina = m_gallona * 3.785
        print(f"{litroina} litraa")
        m_gallona = int(input("Montako gallonaa: \n"))

m_gallona = int(input("Montako gallonaa: \n"))
lasku(m_gallona)