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

uusi_auto = Auto("ABC-123", 142, 60, 2000)

uusi_auto.kulje(1.5)

uusi_auto.print_tiedot()

