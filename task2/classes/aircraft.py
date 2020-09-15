from .vehicle import Vehicle
from task2.configs.const import WeightDirectory


class Aircraft(Vehicle):
    """КЛАСС САМОЛЕТ"""
    fuel = 300
    fuel_full = 600
    fuel_spend = 0.03
    speed = 500
    passengers = 10
    altitude = 5000
    weight = 10
    weight_type = WeightDirectory.TN

    def __init__(self, speed, passengers, **kwargs):
        if speed < 0:
            raise ValueError('Скорость не может быть меньше нуля')

        self.speed = speed
        self.passengers = passengers

        if 'name' in kwargs:
            self.name = kwargs['name']

        if 'altitude' in kwargs:
            self.altitude = kwargs['altitude']

    def __str__(self):
        return f'{self.get_name()}: пассажирова={self.passengers}, скорость={self.get_speed()}'

    def get_name(self):
        return 'Самолет' if self.name is None else self.name


class CargoAircraft(Aircraft):
    """КЛАСС ГРУЗОВОЙ САМОЛЕТ"""
    fuel = 700
    speed = 800
    altitude = 7000
    passengers = 10
    weight = 60

    products = []
    lifting_capacity = 100

    def __str__(self):
        return f'{self.get_name()}: грузоподъемность={self.lifting_capacity} т, скорость={self.get_speed()}'

    def get_name(self):
        return 'Грузовой самолет' if self.name is None else self.name

    def set_products(self, products):
        self.products = products

    def supply(self, city_from, city_to):
        if len(self.products) == 0:
            print(f'Маршрут {city_from.value} - {city_to.value}. Укажите товары для перевозки')
            return False

        result = super().go(city_from, city_to)

        if result is True:
            print(f'Перевозка товаров: {self.products} прошла успешно')
            self.products = []

        return result
