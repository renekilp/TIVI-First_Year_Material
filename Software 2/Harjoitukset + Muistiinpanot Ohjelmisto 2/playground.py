class Koira():

    koirat = 0

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        Koira.koirat = Koira.koirat + 1

    def koirainfo(self):
        print(f'Koiran {self.name} sukupuoli on {self.gender}')


koira1 = Koira('Riku', 'Male')
koira2 = Koira('Miia', 'Female')

Koira.koirainfo(koira1)
Koira.koirainfo(koira2)

print(Koira.koirat)


class Susi(Koira):
    def __init__(self, name, gender, type):
        self.type = type
        super().__init__(name, gender)

    def koirainfo(self):
        super().koirainfo()
        print(f'Koiran tyyppi on {self.type}')


susi1 = Susi('Roki', 'Male', 'Susi')

print(Koira.koirat)
susi1.koirainfo()