LUX = "LUX"
A = "A"
B = "B"
C = "C"

ship_class = input("Syötä hyttiluokka: ")
if ship_class == LUX:
    print("LUX on parvekkeellinen hytti yläkannella.")
elif ship_class == A:
        print("A on ikkunallinen hytti autokannen yläpuolella.")
elif ship_class == B:
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif ship_class == C:
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka!")