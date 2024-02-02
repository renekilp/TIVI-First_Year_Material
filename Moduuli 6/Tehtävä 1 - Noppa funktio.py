import random

dice = 0

while dice != 6:
    dice = random.randint(1, 6)
    if dice < 5:    #   Ei printtaa toivottua lukua kaksi kertaa
        print(f"Heittosi oli {dice}")
    else:
        print(f"Heittosi oli {dice}")


