male = "mies"
female = "nainen"

gender = input("Anna sukupuoli:\n")

if gender == male:
    hemoglobin = int(input("Anna hemoglobiini arvo:\n"))
    if hemoglobin >= 195:
        print ("Hemoglobiini arvo vaarallisen korkea!")
    elif hemoglobin <= 134:
        print("Hemoglobiini arvo on vaarallisen alhainen!")
    else :
        print("Hemoglobiini arvo on normaali.")
if gender == female:
    hemoglobin = int(input("Anna hemoglobiini arvo:\n"))
    if hemoglobin >= 175:
        print ("Hemoglobiini arvo vaarallisen korkea!")
    elif hemoglobin <= 117:
        print("Hemoglobiini arvo on vaarallisen alhainen!")
    else :
        print("Hemoglobiini arvo on normaali.")



