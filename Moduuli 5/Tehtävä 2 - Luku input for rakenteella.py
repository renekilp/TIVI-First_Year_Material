number_list = []

while True:
    number_input = input("Syötä numero (laita tyhjä rivi lopettaaksesi:\n")
    if number_input == "":
        break
    else:
        number = int(number_input)
        number_list.append(number)

number_list.sort(reverse=True)
print(f"Syöttämäsi numerot isoimmasta pienimpään:\n{number_list[:5]}")
