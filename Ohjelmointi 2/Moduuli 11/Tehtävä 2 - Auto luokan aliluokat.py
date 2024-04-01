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


class Sahkoauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti, nopeus=0, matka=0):
        super().__init__(rekisteri, huippunopeus, nopeus, matka)
        self.akkukapasiteetti = akkukapasiteetti

    def lataa(self, lataus):
        self.akkukapasiteetti += lataus

    def tulosta_tiedot(self):
        super().print_tiedot()
        print(f"Akkukapasiteetti: {self.akkukapasiteetti} kWh")


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, bensatankki, nopeus=0, matka=0):
        super().__init__(rekisteri, huippunopeus, nopeus, matka)
        self.bensatankki = bensatankki

    def tankkaa(self, litrat):
        self.bensatankki += litrat

    def tulosta_tiedot(self):
        super().print_tiedot()
        print(f"Bensatankin koko: {self.bensatankki} l")


auto1 = Sahkoauto("ABC-15", 160, 52.5)
auto2 = Polttomoottoriauto("ACD-123", 130, 32.3)

auto1.kiihdyta(120)
auto2.kiihdyta(110)

for _ in range(3):
    auto1.kulje(1)
    auto2.kulje(1)

print(f"Sähköauton ajama matka:\n{auto1.matka} km")
print(f"Polttomoottoriauton ajama matka:\n{auto2.matka} km")