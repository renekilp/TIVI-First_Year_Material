seasons = ("Talvi", "Kevät", "Kesä", "Syksy")

month_input = int(input("Syötä kuukauden numero:\n"))

if month_input <= 0 or month_input > 12:
    print(f"Syöttämäsi kuukauden numero on virheellinen!")
elif month_input <= 3:
    print(f"Vuodenaika on {seasons[0]}")
elif 3 < month_input <= 6:
    print(f"Vuodenaika on {seasons[1]}")
elif 6 < month_input <= 9:
    print(f"Vuodenaika on {seasons[2]}")
else:
    print(f"Vuodenaika on {seasons[3]}")

