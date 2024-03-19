import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

def coord_search(ICAO):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident= '{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

icao1 = coord_search(input("Syötä ensimmäinen ICAO-koodi:\n"))
icao2 = coord_search(input("Syötä toinen ICAO-koodi:\n"))

distance = geodesic(icao1, icao2).kilometers

print(f"Valitsemiesi lentokenttien välinen matka on:\n{distance:.2f} kilometriä.")

