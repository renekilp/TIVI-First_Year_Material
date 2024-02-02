gallons = 0
liters = 0
def liters_to_gallons(liters):
    liters = gallons * 3.785
    return liters

while True:
    gallons = int(input("Syötä bensiinin määrä gallonoina:\n"))
    print(f"Syöttämäsi bensiini määrä litroina:\n{liters_to_gallons(liters)}")
    if gallons < 0:
        break




