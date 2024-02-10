import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)


def find_country_by_code(iso_code):
    sql = f"SELECT name, continent FROM country WHERE iso_country = '{iso_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result
    return

country = find_country_by_code('FI')
print(f"Löydetty maa on: {country}")



