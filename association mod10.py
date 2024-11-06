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
#ex1
'''
class Elevator :
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    def floor_up(self):
        self.current_floor = min(self.top_floor,self.current_floor+1)
        print(f'The floor is {self.current_floor}')
        return
    def floor_down(self):
        self.current_floor = max(self.bottom_floor,self.current_floor-1)
        print(f'The floor is {self.current_floor}')
    def go_to_floor(self,floor):
        check=True
        if floor<self.bottom_floor or floor >self.top_floor:
            print('Out of range .Try Again')
            check=False
        while self.current_floor<floor and check :
            self.floor_up()
        while self.current_floor>floor and check :
            self.floor_down()

el1=Elevator(5,100)
a=el1.floor_up()
print(a)

#ex2
class Building:


    def __init__(self, bottom_floor, top_floor, total_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.total_elevators = total_elevators
        self.Elevators = []
        for i in range(total_elevators + 2) :
            self.Elevators.append(Elevator(bottom_floor, top_floor))


    def run_elevator(self, elevator_num, destination):
        self.Elevators[elevator_num + 1].go_to_floor(destination, elevator_num)


    def fire_alarm(self) :
        for i in range(self.total_elevators) :
            self.run_elevator(i + 1, self.bottom_floor)
        print("All elevators have been evacuated")

Tower = Building(1, 100, 10)
Tower.run_elevator(2, 5)
Tower.run_elevator(3, 9)
Tower.run_elevator(8, 3)
Tower.run_elevator(10, 4)
Tower.fire_alarm()

'''
#ex4
class Car:

    def __init__(self,  license_, max_speed):
        self.current_speed = 0
        self.travelled_distance = 0
        self.license = license_
        self.max_speed = max_speed


    def accelerate(self, _a_) : #_a_ == acceleration
        self.current_speed = max(0, self.current_speed + _a_)
        self.current_speed = min(self.current_speed, self.max_speed)


    def emergency_brake(self) :
        self.accelerate(-200)


    def drive(self, hours) :
        self.travelled_distance += hours * self.current_speed


    def output_properties(self):
        print(self.current_speed, end = " ")
        print(self.travelled_distance, end = ' ')
        print(self.license, end = ' ')
        print(self.max_speed, end = '\n')

import random
class Race :


    def __init__(self, name, kilometers, list_of_cars):
        self._hour_passed = 0
        self._name = name
        self._distance = kilometers
        self._list_of_cars = list_of_cars
        self._total_cars = len(list_of_cars)

    def hour_passes(self):
        for i in range(self._total_cars):
            self._list_of_cars[i].accelerate(random.randint(-10, 15))
            self._list_of_cars[i].drive(1)

        self._hour_passed += 1


    def print_status(self):
        print(f"Hour {self._hour_passed}")
        print(f"{'No.' :^5}| Registration Number | Current speed | Travelled distance | Max Speed | ")
        for i in range(self._total_cars):
            print(f"{i + 1 : ^5}| "
                  f"{self._list_of_cars[i].license:^20}|"
                  f"{self._list_of_cars[i].current_speed :^15}|"
                  f"{self._list_of_cars[i].travelled_distance:^20}|"
                  f"{self._list_of_cars[i].max_speed :^11}|")

    def race_finished(self):
        for i in range(self._total_cars) :
            if self._list_of_cars[i].travelled_distance >= self._distance :
                return True

        return False

cars = [Car(0, 0)] * 10
for i in range(10) :
    individualMaxSpeed = random.randint(100, 200)
    cars[i] = Car(f"ABC-{i + 1}", individualMaxSpeed)

Main_Race = Race("Grand Demolition Derby", 8000, cars)

while Main_Race.race_finished() == 0 :
    Main_Race.hour_passes()

    if(Main_Race._hour_passed % 10 == 0) :
        Main_Race.print_status()
        print()

print("The race has ended.")
Main_Race.print_status()