import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)


def airport_type(iso_code):
    sql = f"SELECT type FROM airport WHERE iso_country = '{iso_code}' ORDER BY type"
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    type_result = {"balloonport": 0, "closed": 0, "heliport": 0,
                   "large_airport": 0, "medium_airport": 0, "small_airport": 0, "seaplane_base": 0}
    for result in results:
        type_find = result[0]
        if type_find in type_result:
            type_result[type_find] += 1
    return type_result


iso_code = input("Syötä maakoodi:\n").upper()
airport_type = airport_type(iso_code)

print(airport_type)


