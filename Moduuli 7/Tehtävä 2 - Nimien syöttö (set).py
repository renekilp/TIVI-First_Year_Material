name_list = set()


def add_names():
    while True:
        new_name = input("Syötä nimi:\n")
        if new_name == "":
            break
        elif new_name in name_list:
            print(f"Aiemmin syötetty nimi!")
        elif name_list.add(new_name):
            print(f"Uusi nimi!")
    return name_list


add_names()
print(f"Tässä kaikki syöttämäsi nimet:\n{name_list}")



