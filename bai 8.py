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
