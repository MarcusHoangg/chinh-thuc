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
''''''
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
#
dt1={'suman' : 89,'minh':90,'long':86,'hoang':91,'olga':90
total=sum(dt1.values())



