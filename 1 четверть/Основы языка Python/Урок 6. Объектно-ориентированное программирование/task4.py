class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Поехала")

    def stop(self):
        print("Остановилась")

    def turn(self, direction):
        print(f"Повернула {direction}")

    def show_speed(self):
        print(f"Скорость автомобиля: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print("Превышение скорости")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print("Превышение скорости")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


print("\nПервая машина TownCar")
first_car = TownCar(70, "Зеленый", "MB", False)
first_car.go()
first_car.stop()
first_car.turn("налево")
first_car.show_speed()

print("\nВторая машина SportCar")
second_car = SportCar(100, "Красный", "Lamb", False)
second_car.go()
second_car.stop()
second_car.turn("направо")
second_car.show_speed()

print("\nТретья машина WorkCar")
third_car = WorkCar(50, "Черный", "Toyota", False)
third_car.go()
third_car.stop()
third_car.turn("направо")
third_car.show_speed()

print("\nЧетвертая машина PoliceCar")
fourth_car = PoliceCar(150, "Черный", "Ford")
fourth_car.go()
fourth_car.stop()
fourth_car.turn("налево")
fourth_car.show_speed()
