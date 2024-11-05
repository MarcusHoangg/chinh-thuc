'''
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        return f"{self.name}, {self.age}, {self.gender}"
class Student(Person):
    def __init__(self, name, age, gender, Student_id):
        super().__init__(name,age,gender)
        self.Student_id = Student_id
    def introduce(self):
        return(f'i am {self.name},my age is {self.age},my gender is {self.gender}  and my ID is {self.Student_id}')
#student1=Student('<NAME>','18','Male',12345)
#print(student1.introduce())
#ver2
class Assistant(Student):
    def __init__(self, name, age, gender, Student_id,assistant_id):
        super().__init__(name,age,gender,Student_id)
        self.assistant_id = assistant_id
    def introduce(self):
        return f'my name is {self.name}, and my assistant id is {self.assistant_id}'
assistant1=Assistant('<NAME>','18','Male',12345,12345)
print(assistant1.introduce())
'''

'''
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
class Student(Person):
   def __init__(self, name, age, gender,student_id):
       super().__init__(name,age,gender)
       self.student_id = student_id
   def introduce(self):
       return f"my name is{self.name}, and my age is {self.age}, and my gender is {self.gender}and my ID is {self.student_id}"
class Teacher(Person):
    def __init__(self, name, age, gender,title ):
        super().__init__(name,age,gender)
        self.title = title
    def introduce(self):
        return f'my name is {self.name}, and my age is {self.age}, and my gender is {self.gender} and my title is {self.title}'
student1=Student('<NAME>','18','Male',12345)
print(student1.introduce())=
teacher1=Teacher('<NAME>','18','Male','lecturer')
print(teacher1.introduce())
'''
'''
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    pass
    def get_age(self):
        return self.get_age
    def get_gender(self):
        return self.get_gender
    def setName(self,name):
        self.name=name
student1=Person("<NAME>","18","Male")
'''

'''
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        return f'my name is {self.name}, and my age is {self.age}, and my gender is {self.gender}'
class Member(Person):
    def __init__(self, name, age, gender,member_id):
       super().__init__(name,age,gender)
       self.member_id = member_id
    def introduce(self):
        return f'my name is {self.name}, and my age is {self.age}, and my gender is {self.gender} and my member_id is {self.member_id}'
class Author(Person) :
    def __init__(self, name, age, gender,books_written):
        super().__init__(name,age,gender)
        self.books_written = books_written
    def list_books(self):
        return f"books written:{'.'.join(self.books_written)}"
class Author_member(Member,Author):
    def __init__(self, name, age, gender,member_id,books_written):
        Person.__init__(self,name,age,gender)
        self.member_id = member_id
        self.books_written = books_written

    def introduce(self):
       return f'my name is {self.name}, and my age is {self.age}, and my gender is {self.gender} and my member_id is {self.member_id} and i have written {self.books_written}'

s1=Author_member('<NAME>','18','Male',12345,12345)
print(s1.introduce())
'''


#EX1
'''
class Publication:
    def __init__(self,name):
        self.name = name
class Book(Publication):
    def __init__(self,name,author,page_cnt):
        Publication.__init__(self,name)
        self.author = author
        self.page_cnt = page_cnt
    def print_information(self):
            print(f"Book's name {self.name},author's name is {self.author},page_cnt is {self.page_cnt}")
class Magazine(Publication):
    def __init__(self,name,chief_editor):
        Publication.__init__(self,name)
        self.chief_editor = chief_editor
    def print_information(self):
        print(f"Magazine's name is {self.name},chief_editor is {self.chief_editor}")
pub1=Magazine('Donald Truck ','Aki Hyyppa')
pub2=Book("Compartment No. 6", "Rosa Liksom", 192)
pub1.print_information()
pub2.print_information()
'''
#EX2
'''
class Car:

    def __init__(self,  license, max_speed):
        self.current_speed = 0
        self.travelled_distance = 0
        self.license = license
        self.max_speed = max_speed


    def accelerate(self, _a_) : #_a_ == acceleration
        self.current_speed = max(0, self.current_speed + _a_)
        self.current_speed = min(self.current_speed, self.max_speed)


    def emergency_brake(self) :
        self.accelerate(-200)


    def drive(self, hours) :
        self.travelled_distance += hours * self.current_speed


    def output_properties(self):
        print(f"License plate: {self.license}")
        print(f"Max speed: {self.max_speed}km/h")
        print(f"Current speed: {self.current_speed}km/h")
        print(f"Travelled distance: {self.travelled_distance}km\n")

class ElectricCar(Car) :

    def __init__(self, license, max_speed, battery_capacity) :
        Car.__init__(self, license, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car) :

    def __init__(self, license, max_speed, tank_volumn) :
        Car.__init__(self, license, max_speed)
        self.tank_volumn = tank_volumn

Car1 = ElectricCar("ABC-15", 180, 52.5)
Car2 = GasolineCar("ACD-123", 165, 32.3)

import random as rand
Car1.current_speed = rand.randint(100, 200)
Car2.current_speed = rand.randint(100, 200)

Car1.drive(3)
Car2.drive(3)

Car1.output_properties()
Car2.output_properties()
'''

