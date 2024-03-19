airport_data = {"KBAB": "Beale Air Force Base", "KBAD": "Barkdsdale Air Force Base", "MRBC": "Barra del Colorado"}
icao_code = None
airport_name = None

while True:
    user_choice = input("Haluatko lisätä, hakea vai lopettaa? Käytä seuraavia komentoja (lisää, haku, lopeta):\n")
    if user_choice == "lopeta":
        break
    elif user_choice == "lisää":
        icao_code = input("Syötä lentokentän ICAO-koodi:\n").upper()
        airport_name = input("Syötä lentokentän nimi:\n")
        airport_data[icao_code] = airport_name
    elif user_choice == "haku":
        icao_input = input("Syötä etsimäsi kentän ICAO-koodi:\n").upper()
        if icao_input in airport_data:
            print(f"Syöttämälläsi koodilla {icao_input} löytyi lentokenttä {airport_data[icao_input]}")

