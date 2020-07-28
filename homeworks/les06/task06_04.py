"""
4.
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""


class Car:
    speed = 0
    color = 0
    name = ''
    is_police = False

    def go(self):
        print(f'{self.name} is driving')

    def stop(self):
        self.speed = 0
        print(f'{self.name} is stopping')

    def turn(self, direction):
        print(f'{self.name} is turning {direction}')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')

    def get_properties(self):
        """
        Добавил функццию для более удобной печати свойств объектов (кроме скорости), в виде списка
        :return:
        """
        return [self.name, self.color, self.is_police]


class TownCar(Car):
    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} speed is too much')


class SportCar(Car):
    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} speed is too much')


class PoliceCar(Car):
    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.is_police = True


# Создаем и катаем городской автомобиль
town_car = TownCar('volvo', 'gray')
print(f'{type(town_car)}: {town_car.get_properties()}')
town_car.go()
town_car.speed = 20
town_car.show_speed()
town_car.turn('right')
town_car.speed = 65
town_car.show_speed()
town_car.stop()
town_car.show_speed()


# Создаем и катаем рабочий автомобиль
work_car = WorkCar('ford', 'yellow')
print(f'{type(work_car)}: {work_car.get_properties()}')
work_car.go()
work_car.speed = 10
work_car.show_speed()
work_car.turn('left')
work_car.speed = 30
work_car.turn('right')
work_car.speed = 45
work_car.show_speed()
work_car.stop()
work_car.show_speed()


# Создаем и катаем спортивный автомобиль
sport_car = SportCar('bmw', 'red')
print(f'{type(sport_car)}: {sport_car.get_properties()}')
sport_car.go()
sport_car.speed = 40
sport_car.show_speed()
sport_car.turn('right')
sport_car.speed = 70
sport_car.show_speed()
sport_car.turn('right')
sport_car.speed = 100
sport_car.show_speed()
sport_car.stop()
sport_car.show_speed()


# Создаем и катаем полицейский автомобиль
police_car = PoliceCar('lincoln', 'white-blue')
print(f'{type(police_car)}: {police_car.get_properties()}')
police_car.go()
police_car.speed = 40
police_car.show_speed()
police_car.stop()
police_car.show_speed()
police_car.go()
police_car.speed = 80
police_car.show_speed()
police_car.turn('right')
police_car.turn('left')
police_car.turn('right')
police_car.speed = 100
police_car.show_speed()
police_car.stop()
police_car.show_speed()

