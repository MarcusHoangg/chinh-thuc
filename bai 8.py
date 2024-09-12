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

# Main program
connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='database class',
         user='minhdbb',
         password='quangminh2006',
         autocommit=True,
         charset='utf8mb4',
         collation="utf8mb4_general_ci",)
last_name = input("Enter last name: ")
get_employees_by_last_name(last_name)
