import random

dice_count = int(input("Kuinka monta noppaa haluat heittää: \n"))
dice_sum = 0

for i in range(dice_count):
    dice = random.randint(1, 6)
    dice_sum += dice

print(f"Heitettyjen noppien summa: {dice_sum}\n")