number_list = []

while True:
    number_str = input("Syötä numero:\n")
    number = int(number_str)
    number_list.append(number)
    if number == "":
        number_list.sort(reverse=True)
        break
print(number_list[:5])
 #  TEE LOPPUUN!