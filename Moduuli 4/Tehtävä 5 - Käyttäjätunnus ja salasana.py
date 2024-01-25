i = 0
right_usern = "python"
right_pass = "rules"
username_input = None
password_input = None

while username_input != right_usern or password_input != right_pass :
    username_input = input("Syötä käyttäjä tunnus:\n")
    password_input = input("Syötä salasana:\n")
    i += 1
    if i == 5:
        print("Pääsy evätty.")
        break
    if username_input == right_usern and password_input:
        print("Tervetuloa!")




