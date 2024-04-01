class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros

    def siirry_ylos(self):
        self.kerros += 1

    def siirry_alas(self):
        self.kerros -= 1

    def siirry_kerrokseen(self, kerrokseen):
        print("-" * 30)
        print(f"Lähtö kerros:\n{self.kerros}")
        if kerrokseen < self.kerros:
            while kerrokseen < self.kerros:
                self.siirry_alas()
                print("-" * 30)
                print(f"Siirrytään kerrokseen:\n{self.kerros}")
        else:
            while kerrokseen > self.kerros:
                self.siirry_ylos()
                print("-" * 30)
                print(f"Sirrytään kerrokseen:\n{self.kerros}")
        print("-" * 30)
        print(f"Pysähdys kerros:\n{self.kerros}")


hissi1 = Hissi(0, 5)

hissi1.siirry_kerrokseen(4)
hissi1.siirry_kerrokseen(0)










