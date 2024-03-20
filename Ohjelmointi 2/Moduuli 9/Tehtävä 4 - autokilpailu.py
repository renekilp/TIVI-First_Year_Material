import random

class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus=0, matka=0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def print_tiedot(self):
        print(f"Auton: {self.rekisteri}\nHuippunopeus: {self.huippunopeus} km/h\nTämän hetkinen nopeus: {self.nopeus} km/h\nTähän asti tehty matka: {self.matka} km")

    def kiihdyta(self, muutos):
        if muutos > 0:
            self.nopeus = min(self.nopeus + muutos, self.huippunopeus)
        else:
            self.nopeus = max(self.nopeus + muutos, 0)

    def kulje(self, aika):
        kuljettumatka = self.nopeus * aika
        self.matka += kuljettumatka

autot = []
for i in range(10):
    rekisteri = f"ABC-{i+1}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteri, huippunopeus))

autokilpailu = True
while autokilpailu:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)
        if auto.matka >= 10000:
            autokilpailu = False
            break

for auto in autot:
    print("-"*33)
    auto.print_tiedot()

