#Tuple

'''
day_of_the_week =("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
day_number=int(input("Enter the day number(1-7): "))
day=day_of_the_week[day_number-1]
print(f'the day {day_number} is {day}')
'''
'''
fruits = "Orange", "Banana", "Apple"
print(fruits)
'''
#Tuple unpacking
'''
fruits = "Orange", "Banana", "Apple"
(first, second, third) = fruits
print(f"The fruits are: {first}, {second} and {third}.")
'''
#Tuples as return values
'''
import random 
def cast():
     first,second=random.randint(1,6),random.randint(1,6)
     return first,second
dice1,dice2=cast()
print(f"the dice show is {dice1} and {dice2}")
'''
#
'''''
students={"poon","suzy","sharmila","shorstika"}
print(type(students))
print(students)
students.add("sailesh")
print(students)
students.add("frimpong")
print(students)
students.remove("sailesh")
print(students)
'''
#exercise
#ex1
'''
seasons=("WINTER","WINTER","SPRING","SPRING","SUMMER","SUMMER","SUMMER","AUTUMN","AUTUMN","AUTUMN","WINTER")
month=int(input("Enter the month number: "))
if 1 <=month<=12:
    print(f'month is {month} related to {seasons[month-1]}')
'''
#ex2
'''
name_set=set()
while True:
    user_input=input("Enter the name of a person(or press enter to exit): ")
    if user_input =="":
        break
    if user_input  in name_set:
        print("name existed")
    else:
        print(f'new name{user_input}')
        name_set.add(user_input)
    print("list of name entered")
    for nme in name_set:
        print(name)
'''
#ex3
'''
airport={}
command=input("type 'add' to add a new airport,;'view'to find an airport or 'quit' to quit the program :")
while command !="quit":
    if command =="add":
        airport_name=input("Enter the name of the airport: ")
        airport_ICAO=input("Enter the ICAO code: ").upper()
        airport_list[airport_ICAO]=airport_name
    elif command =="view":
        airport_view=input("Enter the ICAO code of the airport: ")
        if airport_view in airport_list:
            print(f'the airport with {airport_view} code is airport{airport_list[airport_view]}'')
        else:
            print("airport not found")
    else:
            print("invalid command")
    command = input("type 'add' to add a new airport,;'view'to find an airport or 'quit' to quit the program :")
'''




