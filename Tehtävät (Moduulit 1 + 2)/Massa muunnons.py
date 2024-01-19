first = input("Syötä luotien määrä: \n")
second = input("Syötä naulojen määrä: \n")
third = input("Syötä leivisköjen määrä: \n")

luoti_weight = float(first)
naula_weight = float(second)
leivis_weight = float(third)
massa = 13.3 * ((leivis_weight * 20 + naula_weight) * 32 + luoti_weight)

print(f"Massa nykymittojen mukaan:\n{int(massa / 1000)} kilogrammaa ja {int(massa % 1000)} grammaa.")













