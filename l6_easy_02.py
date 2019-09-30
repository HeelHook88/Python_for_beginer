
class AllCar:
    def  __init__(self,go,stop,turn_left,turn_right):
        self.go = 'Car is Go'
        self.stop = 'Car is stop'
        self.turn_left = "Car is turn left"
        self.turn_right = "Car is turn Right"

class TownCar(AllCar):

    def speed(self):
        town_car_speed = print("TownCar speed is 60 KM/H")

    def color(self):
        town_car_color = print("TownCar Color is Blue")

    def name(self):
        town_car_name = print("TownCar name is Priora ")

    def is_police(self):
        TownCar_is_police = False
        print(TownCar_is_police)

class SportCar(TownCar):

    def speed(self):
        spopt_car_speed = print("SportCar speed is 260 KM/H")

    def color(self):
        sport_car_color = print("SportCar Color is Green")

    def name(self):
        sport_car_name = print("SportCar name is Lamborgini ")

    def is_police(self):
        sport_car_is_police = False
        print(sport_car_is_police)

class WorkCar(SportCar):

    def speed(self):
        work_car_speed = print("WorkCar speed is 100 KM/H")

    def color(self):
        work_car_color = print("WorkCar Color is Brown")

    def name(self):
        work_car_name = print("WorkCar name is Gazel ")

    def is_police(self):
        work_car_is_police = False
        print(work_car_is_police)

class PoliceCar(WorkCar):

    def speed(self):
        police_car_speed = print("PoliceCar speed is 180 KM/H")

    def color(self):
        police_car_color = print("PoliceCar Color is White")

    def name(self):
        police_car_name = print("PoliceCar name is Police ")

    def is_police(self):
        police_car_is_police = True
        print(police_car_is_police)

newcar = PoliceCar('go', "stop", 'left', 'right', True)

print(newcar.is_police)