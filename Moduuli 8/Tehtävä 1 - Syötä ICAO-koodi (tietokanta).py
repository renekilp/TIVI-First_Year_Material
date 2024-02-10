import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)


user_input = input("Syötä lentokentän ICAO-koodi:\n").upper()
cursor = connection.cursor()
cursor.execute(f"SELECT name, municipality FROM airport WHERE ident= '{user_input}'")
result_row = cursor.fetchone()
print(result_row)



