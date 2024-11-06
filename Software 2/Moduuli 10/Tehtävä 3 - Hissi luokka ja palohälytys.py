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


class Talo:
    def __init__(self, talonalinkerros, talonylinkerros, hissienmaara):
        self.hissit = [Hissi(talonalinkerros, talonylinkerros) for _ in range(hissienmaara)]

    def kayta_hissia(self, hissinumero, kohdekerros):
        print("-" * 30)
        print(f"Ajetaan hissi numero:\n{hissinumero}\nKerrokseen:\n{kohdekerros}")
        self.hissit[hissinumero].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("""
        ███████╗██╗██████╗ ███████╗     █████╗ ██╗      █████╗ ██████╗ ███╗   ███╗██╗
        ██╔════╝██║██╔══██╗██╔════╝    ██╔══██╗██║     ██╔══██╗██╔══██╗████╗ ████║██║
        █████╗  ██║██████╔╝█████╗      ███████║██║     ███████║██████╔╝██╔████╔██║██║
        ██╔══╝  ██║██╔══██╗██╔══╝      ██╔══██║██║     ██╔══██║██╔══██╗██║╚██╔╝██║╚═╝
        ██║     ██║██║  ██║███████╗    ██║  ██║███████╗██║  ██║██║  ██║██║ ╚═╝ ██║██╗
        ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝
        """)
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(0)


talo1 = Talo(0, 7, 2)

talo1.kayta_hissia(1, 5)

talo1.palohalytys()
















