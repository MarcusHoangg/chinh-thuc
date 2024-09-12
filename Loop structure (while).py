#Fixed amount of repetitions
'''
rounds=int(input(f"how many times "))
finished_times = 0
while finished_times < rounds :
    print("good morning")
    finished_times= finished_times+1
'''
#User ends the repetition
'''
command = input("enter command")
while command!="stop" :
    print("executing"+command)
    command = input("enter command:")
print("execution stopped ")
'''
#Varying amount of repetitions
'''
import random
dice1 = dice2 = rolls = 0
while (dice1!=6 or dice2!=6):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls + 1
print(f"Rolled {rolls:d} times.")
'''
# Nested loops
'''
first = 1
while first <= 5:
    second = 1
    while second <= 5:
        print(f"{first} times {second} is {first*second:d}")
        second = second + 1
    first = first + 1
'''
#Break
'''
command = input("enter command")
while command!="stop" :
    if command=="MAYDAY":
        break
    print("executing command  "+command)
    command = input("enter command:")
print("execution stopped ")
'''
# while , else :
'''
command = input("Enter command: ")
while command!="stop":
    if command=="MAYDAY":
        break
    print("Executing command: " + command)
    command = input("Enter command: ")
else:
    print("Goodbye.")
print("Execution stopped.")
'''
#Infinite loop
# Faulty program, infinite loop
'''
number = 1
while number<5:
    print(number)

# This part is never reached:
print("All ready.")
'''