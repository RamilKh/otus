from .vehicle import Vehicle
from task2.configs.const import SpeedDirectory, WeightDirectory, WeatherDirectory
from task2.classesdata import Distance
from task2.exceptions import FuelDeficiencyException, VehicleStateException, WeatherStateException


class Ship(Vehicle):
    """КЛАСС КОРАБЛЬ"""
    fuel = 0
    fuel_full = 500
    fuel_spend = 0.02
    speed = 5
    displacement = 500
    speed_type = SpeedDirectory.KN
    weight = 30
    weight_type = WeightDirectory.TN

    def __init__(self, speed, **kwargs):
        if speed < 0:
            raise ValueError('Скорость не может быть меньше нуля')

        self.speed = speed

        if 'name' in kwargs:
            self.name = kwargs['name']

        if 'fuel' in kwargs:
            self.fuel = kwargs['fuel']

        if 'displacement' in kwargs:
            self.displacement = kwargs['displacement']

    def __str__(self):
        return f'{self.get_name()}: скорость={self.get_speed()}, водоизмещение={self.displacement} т.'

    # поехать
    def go(self, city_from, city_to, weather=None):
        """
        :param city_from: CitiesDirectory - город отправки
        :param city_to: CitiesDirectory - город назначения
        :param weather: WeatherDirectory - погода
        :return: True | False - результат поездки
        """
        try:
            distance = Distance()
            distance_value = distance.get_value(city_from, city_to, self.speed_type)

            spend = self.fuel_spend * distance_value

            if weather is not None and weather in [WeatherDirectory.STORM, WeatherDirectory.RAIN]:
                raise WeatherStateException(
                    f'Маршрут {city_from.value} - {city_to.value}'
                )

            if spend > self.fuel:
                raise FuelDeficiencyException(
                    spend - self.fuel,
                    f'Маршрут {city_from.value} - {city_to.value}'
                )

            self.fuel -= spend
            print(f'Поехали, маршрут: {city_from.value} - {city_to.value}')

        except WeatherStateException as error:
            print(error)
            return False

        except FuelDeficiencyException as error:
            print(error)
            return False

        except Exception as error:
            print(error)
            return False

        return True

    def get_name(self):
        return 'Корабль' if self.name is None else self.name


class MilitaryShip(Ship):
    """КЛАСС ВОЕННЫЙ КОРАБЛЬ"""
    fuel = 400
    speed = 15
    displacement = 10000
    weight = 100
    rockets = 10
    tracing = False

    def __init__(self, speed, rockets=10, **kwargs):
        if speed < 0:
            raise ValueError('Скорость не может быть меньше нуля')

        self.speed = speed
        self.rockets = rockets

        if 'name' in kwargs:
            self.name = kwargs['name']

        if 'displacement' in kwargs:
            self.displacement = kwargs['displacement']

    def get_name(self):
        return 'Военный корабль' if self.name is None else self.name

    def count_rockets(self):
        return self.rockets

    def shoot_rocket(self, rockets=1):
        if self.rockets < rockets:
            print(f'Недостаточно ракет для выстрела')
            return

        self.rockets -= rockets
        print(f'Выстрел из ракеты, осталось ракет: {self.rockets}')

    def trace_enemy(self):
        self.tracing = True
        print('Преследовать врага')

    def stop_trace_enemy(self):
        self.tracing = False
        print('Прекратить преследование врага')
