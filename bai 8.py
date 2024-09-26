'''
import mysql.connector
connection = mysql.connector.connect(
    user="minhdbb",
    password="quangminh2006",
    host="localhost",
    port=3306,
    database="database class",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)
print("connected sucessfully to MariaDB")
'''
''''
import mysql.connector
def get_employees_by_last_name(last_name):
    sql = f"SELECT NUMBER, lastname, firstname, salary FROM employee1 WHERE lastname='{last_name}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
    return
'''
import mysql.connector
# Main program
'''
connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='database class',
         user='minhdbb',
         password='quangminh2006',
         autocommit=True,
         charset='utf8mb4',
         collation="utf8mb4_general_ci",)
def update_salary(number, new_salary):
    sql = f"UPDATE Employee1 SET Salary={new_salary} WHERE Number={number}"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount==1:
        print("Salary updated")
number = int(input("Enter number: "))
new_salary = float(input("Enter new salary: "))
update_salary(number, new_salary)

'''''
#homework
import mysql.connector

def get_airport_info(icao_code):
    query = "select name, municipality from airport where ident = %s"
    cursor = connection.cursor()
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()

    if result:
        name, municipality = result
        print(f"Airport Name: {name}")
        print(f"Location (Town): {municipality}")
    else:
        print("No airport found with the given ICAO code.")

    cursor.close()
    connection.close()
    return

# Establish a connection to the database
connection = mysql.connector.connect(
    user="minhdbb",
    password="quangminh2006",
    host="localhost",
    port="3306",
    database="flight_game",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)

# Prompt the user to enter the ICAO code
icao_code = input("Enter the ICAO code of the airport: ").strip().upper()

get_airport_info(icao_code)


'''
#Write a program that asks the user to enter the area code (for example FI) and prints
# out the airports located in that country ordered by airport type. For example, Finland
# has 65 small airports, 15 helicopter airports and so on.
import mysql.connector
from tabulate import tabulate
def get_airport_by_country(iso_country):
    query = "select name, type from airport where airport.iso_country = %s order by type"
    cursor = connection.cursor()
    cursor.execute(query, (iso_country,))
    result = cursor.fetchall()
    if result:
        print(tabulate(result, headers = ["Name", "Type"], tablefmt="fancy_grid"))
    else:
        print("No airport found with the given ISO country code.")

    cursor.close()
    connection.close()
    return

connection = mysql.connector.connect(
    user="Suman",
    password="Pokhara@2024",
    host="localhost",
    port="3306",
    database="flight_game",
    charset="utf8mb4",
    collation="utf8mb4_general_ci")

iso_country = input("Enter the ISO country code of the airport: ").upper()
get_airport_by_country(iso_country)
'''


'''
#Write a program that asks the user to enter the ICAO codes of two airports. The program
#prints out the distance between the two airports in kilometers. The calculation is based
# on the airport coordinates fetched from the database.

import mysql.connector
from geopy.distance import geodesic

def get_airport_coordinates(icao_code):
    query = "select latitude_deg, longitude_deg from airport where ident = %s"
    cursor = connection.cursor()
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    return result
def calculate_distance(icao1, icao2):
    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if not coords1 or not coords2:
        print("No airport found with the given ICAO code(s).")
        return

    distance = geodesic(coords1, coords2).kilometers
    print(f"The distance between {icao1} and {icao2} is {distance:.2f} kilometers.")
    return distance

connection = mysql.connector.connect(
    user="Suman",
    password="Pokhara@2024",
    host="localhost",
    port="3306",
    database="flight_game",
    charset="utf8mb4",
    collation="utf8mb4_general_ci")

icao1 = input("Enter the ICAO code of the first airport: ").upper()
icao2 = input("Enter the ICAO code of the second airport: ").upper()
calculate_distance(icao1,icao2)
connection.close()
'''