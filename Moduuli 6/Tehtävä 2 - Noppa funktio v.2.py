import random

max_result = int(input("Minkä haluat noppien loppusummaksi?\n"))
dice = 0

def roll_dice(max_result):
    throw = random.randint(1, max_result)
    print(throw)


while dice < max_result:
    dice = random.randint(1, max_result)
    print(f"Heittosi oli {dice}. Toivomasi loppusumma oli {max_result} ")
else:
    print(f"Heittosi oli {dice}")

roll_dice(max_result)