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


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Auto':<15}{'Nopeus (km/h)':<15}{'Matka (km)':<15}")
        for auto in self.autot:
            print(f"{auto.rekisteri:<15}{auto.nopeus:<15}{auto.matka:<15}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False


autot = []
for i in range(10):
    rekisteri = f"ABC-{i+1}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteri, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 1

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    if tunti % 10 == 0:
        print("-" * 40)
        print(f"Tunti {tunti} tilanne:\n")
        kilpailu.tulosta_tilanne()
    tunti += 1

print("-" * 40)
print(f"Kilpailu '{kilpailu.nimi}' on päättynyt! Lopullinen tilanne on:\n")
kilpailu.tulosta_tilanne()
