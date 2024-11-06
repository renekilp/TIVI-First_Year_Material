number_input = int(input("Syötä kokonaisluku:\n"))
prime_number = True

if number_input < 2:
    print(f"Syöttämäsi luku {number_input} ei ole kokonaisluku!")
else:
    for i in range(2, int(number_input ** 0.5) + 1):
        if number_input % i == 0:
            prime_number = False
            print(f"Luku {number_input} ei ole alkeisluku.")
            break
    if prime_number:
        print(f"Luku {number_input} on alkeis luku.")
