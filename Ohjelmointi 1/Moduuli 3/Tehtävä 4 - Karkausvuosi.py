year = int(input("Syötä vuosi:\n"))

if (year % 4 == 0 and year % 100 != 0) :
    print(f"{year} on karkaus vuosi.")
else :
    print(f"{year} ei ole karkausvuosi.")






