import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

cursor = connection.cursor()  # kuvittele kurosi joka valitsee

cursor.execute("SELECT iso_country, name FROM country WHERE name='Finland'")
result_row = cursor.fetchall()  # cursor.fetchone() hakee yhden cursor.fetchall() hakee kaikki
print(f"Ensimmäinen rivi näyttäisi: {result_row[0]}, jossa maakoodi: {result_row[0][0]}")
# [0] tulostaisi pelkän arvon   # tuple jonka sisällä on lista [(,)]
# print(result_row)  tulostaisi seuraavan listalta
print(f"Maakoodeja löytyi: {cursor.rowcount}")
if cursor.rowcount > 0:
    for row in result_row:
        print(f"Maakoodi: {row[0]}, nimi: {row[1]}")
else:
    print("Ei tuloksia.")


#   ei mielellään kirjoiteta tälläistä koodia (käytä funktiota mieluummin)

def find_country_by_code(iso_code):
    sql = f"SELECT name, continent FROM country WHERE iso_country = '{iso_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result
    return

def update_country_by_name_by_code(iso_code, name):
    sql = f"UPDATE country SET name = '{name}' WHERE iso_country = '{iso_code}'"
    #   tarkista että sql on oikein muodostettu MUUTEN MENEE KOKO TIETOKANTA SEKAISIN
    #   print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:
        print(f"Update complete! {iso_code}: {name}")
        return True
    print("Update failed.")


code_input = input("Syötä maakoodi:\n")
country_input = input("Uusi nimi:\n")
update_country_by_name_by_code(code_input, country_input)

country = find_country_by_code(user_input)

if country:
    print(f"Löydetty maa on: {country[0]}, {country[1]}")
else:
    print("Ei tuloksia.")
