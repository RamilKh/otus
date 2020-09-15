from dataclasses import dataclass, field
from typing import List
from task2.configs.const import SpeedDirectory, CitiesDirectory


@dataclass(frozen=True)
class Distance:
    data: List = field(default_factory=list)

    def __post_init__(self):
        self.data.append({'city_from': CitiesDirectory.MOSCOW, 'city_to': CitiesDirectory.PETERBURG,  'KM': 770, 'KN': 415})
        self.data.append({'city_from': CitiesDirectory.MOSCOW, 'city_to': CitiesDirectory.NOVGOROD,  'KM': 400, 'KN': 215})
        self.data.append({'city_from': CitiesDirectory.MOSCOW, 'city_to': CitiesDirectory.SAMARA, 'KM': 1100, 'KN': 595})
        self.data.append({'city_from': CitiesDirectory.MOSCOW, 'city_to': CitiesDirectory.TUMEN, 'KM': 2100, 'KN': 1135})

        self.data.append({'city_from': CitiesDirectory.PETERBURG, 'city_to': CitiesDirectory.NOVGOROD, 'KM': 1100, 'KN': 595})
        self.data.append({'city_from': CitiesDirectory.PETERBURG, 'city_to': CitiesDirectory.SAMARA, 'KM': 1800, 'KN': 971})
        self.data.append({'city_from': CitiesDirectory.PETERBURG, 'city_to': CitiesDirectory.TUMEN, 'KM': 2800, 'KN': 1510})

        self.data.append({'city_from': CitiesDirectory.NOVGOROD, 'city_to': CitiesDirectory.SAMARA, 'KM': 680, 'KN': 367})
        self.data.append({'city_from': CitiesDirectory.NOVGOROD, 'city_to': CitiesDirectory.TUMEN, 'KM': 1700, 'KN': 917})

        self.data.append({'city_from': CitiesDirectory.SAMARA, 'city_to': CitiesDirectory.TUMEN, 'KM': 1300, 'KN': 701})

    # получить расстоние
    def get_value(self, city_from, city_to, speed_type=SpeedDirectory.KM):
        """
        :param city_from: CitiesDirectory - город отправки
        :param city_to: CitiesDirectory - город назначения
        :param speed_type: тип расстояния (км или мили)
        :return:
        """
        for city in self.data:
            if (city['city_from'] == city_from and city['city_to'] == city_to) or \
                    (city['city_to'] == city_from and city['city_from'] == city_to):
                return city[speed_type.name]

    # добавить дистанцию
    def add_value(self, city_from, city_to, km, kn):
        self.data.append({'city_from': city_from, 'city_to': city_to, 'KM': km, 'KN': kn})
