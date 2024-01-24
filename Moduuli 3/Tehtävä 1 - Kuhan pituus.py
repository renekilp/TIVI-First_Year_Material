kuha_input = int(input("Syötä kuhan pituus senttimetreinä:\n"))
ideal_lenght = 37

if kuha_input <= ideal_lenght:
    print(f"Kuha on liian pieni!\nSallitusta pyyntimitasta puuttuu {ideal_lenght - kuha_input} cm.\nVapauta kuha takaisin veteen.")
else:
    print("Kuha on ideaalimittainen!")