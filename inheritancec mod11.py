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