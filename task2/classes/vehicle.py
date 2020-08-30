from task2.utils.common import plural_speed
from task2.configs.const import SpeedDirectory, WeightDirectory, StateDirectory
from task2.classesdata import Distance
from task2.exceptions import FuelDeficiencyException, VehicleStateException
from abc import ABCMeta, abstractmethod


class VehicleABC(metaclass=ABCMeta):
    """Абстрактный класс для базового класса средства передвижения"""

    @staticmethod
    @abstractmethod
    def get_distance(self):
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def get_name(self):
        raise NotImplemented

    @abstractmethod
    def get_name(self):
        raise NotImplemented

    @abstractmethod
    def get_speed(self):
        raise NotImplemented

    @abstractmethod
    def go(self):
        raise NotImplemented

    @abstractmethod
    def refuel(self):
        raise NotImplemented

    @abstractmethod
    def repair(self):
        raise NotImplemented

    @abstractmethod
    def extreme(self):
        raise NotImplemented


class Vehicle(VehicleABC):
    """Базовый класс для средства передвижения"""
    name = None
    state = StateDirectory.OK
    fuel = 0
    fuel_full = 0
    fuel_spend = 0

    speed = 0
    speed_type = SpeedDirectory.KM

    weight = 0
    weight_type = WeightDirectory.KG

    city = None

    def __str__(self):
        return f'{self.get_name()}: {self.get_speed()}'

    def __repr__(self):
        return str(self)

    def get_name(self):
        return 'Транспорт'

    # рассчитать расстояние
    def get_distance(self, city_from, city_to):
        distance = Distance()
        value = distance.get_value(city_from, city_to, self.speed_type)
        spend = self.fuel_spend * value

        return value, spend

    # получить скорость транспорта
    def get_speed(self):
        return str(self.speed) + ' ' + plural_speed(self.speed, self.speed_type)

    # поехать
    def go(self, city_from, city_to, extreme=False):
        """
        :param city_from: CitiesDirectory - город отправки
        :param city_to: CitiesDirectory - город назначения
        :param extreme: экстремальное вождение (попал в аварию, ломает автомобиль)
        :return: True | False - результат поездки
        """
        try:
            distance, spend = self.get_distance(city_from, city_to)

            if self.state != StateDirectory.OK:
                raise VehicleStateException(
                    f'Маршрут {city_from.value} - {city_to.value}'
                )

            if spend > self.fuel:
                raise FuelDeficiencyException(
                    spend - self.fuel,
                    f'Маршрут {city_from.value} - {city_to.value}'
                )

            self.fuel -= spend
            self.city = city_to
            print(f'Поехали, маршрут: {city_from.value} - {city_to.value}')

            if extreme is True:
                self.extreme()

        except VehicleStateException as error:
            print(error)
            return False

        except FuelDeficiencyException as error:
            print(error)
            return False

        except Exception as error:
            print(error)
            return False

        return True

    # заправиться
    def refuel(self, value=None):
        if value is None:
            self.fuel = self.fuel_full
        else:
            self.fuel += value

        print(f'Заправились, топливо: {self.fuel} л.')

    # починить
    def repair(self):
        if self.state == StateDirectory.REPAIRING:
            self.state = StateDirectory.OK
            print(f'Отремонтировали')
        else:
            print(f'Уже отремонтировали')

    # поломать
    def extreme(self):
        self.state = StateDirectory.REPAIRING
        print(f'Поломались')

