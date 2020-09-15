from .vehicle import Vehicle
from task2.configs.const import Color
from task2.exceptions import FuelDeficiencyException


class Car(Vehicle):
    """КЛАСС АВТОМОБИЛЬ"""
    fuel = 0
    fuel_full = 150
    fuel_spend = 0.05
    speed = 120
    wheels = 4
    color = Color.GRAY
    weight = 1000

    def __init__(self, speed, color, **kwargs):
        if speed < 0:
            raise ValueError('Скорость не может быть меньше нуля')

        self.speed = speed
        self.color = color
        self.fuel = self.fuel_full

        if 'name' in kwargs:
            self.name = kwargs['name']

        if 'wheels' in kwargs:
            self.wheels = kwargs['wheels']

    def __str__(self):
        return f'{self.get_name()}: цвет={self.color.value}, скорость={self.get_speed()}'

    def get_name(self):
        return 'Автомобиль' if self.name is None else self.name


class AutoCar(Car):
    """КЛАСС ЛЕГКОВОЙ АВТОМОБИЛЬ"""
    fuel = 40
    speed = 140
    color = Color.WHITE
    starting = False

    def get_name(self):
        return 'Легковой автомобиль' if self.name is None else self.name

    def start(self):
        try:
            if self.fuel == 0:
                raise FuelDeficiencyException(
                    None,
                    'Завести'
                )

            self.starting = True
            print('Завели')

        except FuelDeficiencyException as error:
            print(error)
            return False

        except Exception as error:
            print(error)
            return False

        return True

    def stop(self):
        print('Выключили мотор')
        self.starting = False

    def go(self, city_from, city_to):
        if self.starting is True:
            return super().go(city_from, city_to)

        print(f'Маршрут {city_from.value} - {city_to.value}. Перед поездкой нужно завести')
        return False


class BusCar(Car):
    """КЛАСС МАРШРУТНЫЙ АВТОМОБИЛЬ"""
    fuel = 50
    speed = 120
    color = Color.WHITE
    weight = 2000

    def get_name(self):
        return 'Маршрутный автомобиль' if self.name is None else self.name

    def get_position(self):
        return self.city
