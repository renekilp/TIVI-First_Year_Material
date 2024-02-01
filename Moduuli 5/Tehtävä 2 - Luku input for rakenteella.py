number_list = []

while True:
    number_str = input("Syötä numero:\n")
    if number_str == "":
        break

number = int(number_str)
number_list.append(number)
number_list.sort(reverse=True)

print(number_list[:5])
 #  TEE LOPPUUN!