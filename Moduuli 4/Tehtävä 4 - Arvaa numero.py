import random

num = random.randint(1,10)
user_guess = 0

while True:
    user_guess = int(input("Arvaa numero 1-10:\n"))
    if user_guess > num:
        print("Liian suuri arvaus.")
    if user_guess < num:
        print("Liian pieni arvaus.")
    if user_guess == num:
        print("Arvasit numeron!")
        break