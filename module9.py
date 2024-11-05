'''
class Dog:
  pass
# We create a myDog object , constructor

mydog = Dog()
mydog.name='chicko'
mydog.age='2'
print(mydog.name, mydog.age)

yourdog=Dog()
yourdog.name='mi'
yourdog.age='3'
print(yourdog.name,yourdog.age)
'''

'''
class Dog:
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Dog.count+=1
#setter and getter to manipulate th content of the attribute
    def change_name(self,name):
        self.name=name
    def getName(self):
        return self.name
    def getAge(self,age):
        return self.age
    def __str__(self):
        return f'{self.name} {self.age}'


mydog=Dog('chicko',3)
yourdog=Dog("mi",2)
print(f'Dog name:{mydog.name} is {mydog.age} years old')
mydog.change_name('mikko')
yourdog.change_name('opo')
print({mydog.name})
print({mydog.getAge})
print(str(mydog))
print(Dog.count)
'''
'''
class Nursing:
    def __init__(self):
        self.dog=[]
    def addDog(self,name):
        self.dog.append(dog(name))
        print(f"the{self.dog} id added")
    def getDog(self ):
        for dog in self.dog:
            print(dog.getName(),dog.getAge())
'''




'''
class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)
        return

class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print(dog.name + " checked in")
        return

    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print(dog.name + " checked out")
        return

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)

# Main program

dog1 = Dog("Rascal", 2018)
dog2 = Dog("Boi", 2022, "Yip yip yip")

hotel = Hotel()

hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.greet_dogs()

hotel.dog_checkout(dog1)
hotel.greet_dogs()
'''
'''
class Student_class:
    count=0
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        Student_class.count+=1
        self.course=[]
    def change_name(self,name):
        self.name=name
    def  getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGender(self):
        return self.gender
    def __str__(self):
        return f'({self.name},{self.age},{self.gender})'

studentA=Student_class('Minh',18,'Male')
studentB=Student_class('long',18,'male')
studentC=Student_class('Hoang',18,'male')

class Course:
    def __init__(self,name):
        self.name=name
        self.students=[]
    def addStudent(self,students):
        self.students.append(students)
        print(f'{students} is added to {self.name}')
    def removeStudent(self,students):
        self.students.remove(students)
        print(f'{students} is removed from {self.name}')
    def getStudents(self):
        for student in self.students:
            print(student.getName(),student.getAge())


course1=Course('computer science')
course2=Course('programming')
course3=Course('math')
course1.addStudent(studentA)
course2.addStudent(studentB)
'''
'''
student1=Student_class('Minh',18,'Male')
course=Course()
course.addStudent(student1)
course.getStudents()
'''

#way number2 ex1
'''
registration_Number=input('enter your number:')
maximum_speed=input('enter your maximum speed:')
car=Car(registration_Number,maximum_speed)
print(car.maximum_speed)
print(f'current speed is {car.current_speed}')
print(f'maximum speed is {car.maximum_speed}')
print(f'car distance is {car.distance}')
'''
# for testing
'''
print(f'{registration_number} is registered,{maxi})
newCar = Car('ABC-123', 142)
newCar.accelerate(30)
newCar.accelerate(70)
newCar.accelerate(50)
newCar.EmergencyBrake()
newCar.accelerate(60)
'''
#EX1:
'''
class Car:
    def __init__(self,registration_number, maximum_speed):
        self.registration_number=registration_number
        self.maximum_speed=maximum_speed
        self.current_speed=0
        self.distance=0
#way number 1
    def __str__(self):
         return (f"{self.registration_number},{self.maximum_speed} km/h,{self.current_speed}km/h,{self.distance}km")
    def accelerate(self,change_of_speed):
        self.current_speed = max(0, self.current_speed + change_of_speed)
        self.current_speed = min(self.current_speed, self.maximum_speed)
        if self.current_speed == 0:
            print("The vehicle has come to a full stop.")
        elif change_of_speed == 0:
            print("The car's speed hasn't changed at all.")
        elif change_of_speed > 0:
            print(f"The car's speed have increased to {self.current_speed}.")
        else:
            print(f"The car's speed have decreased to {self.current_speed}.")
    def EmergencyBrake(self):
           self.accelerate(-200)
    def drive(self,hours):
        self.distance+=self.current_speed*hours
        print(f'The car has travelled {self.distance} km ')
def check():
    for C in car :
        if C.distance>=10000:
                return False
    return True
import random

    car=[]
for i in range(10):
    maximum_speed=random.randint(100,200)
    registration_number="ABC"+str(i+1)
    car.append(Car(registration_number,maximum_speed))
while True:
    for i in range(10):
        random_change_speed=random.randrange(-10,15)
        car[i].accelerate(random_change_speed)
        car[i].drive(1)
    if not check():
        break
for i in range(10):
    print(car[i].registration_number, car[i].maximum_speed, car[i].current_speed, car[i].distance)
'''
