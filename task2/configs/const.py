from enum import Enum, unique


@unique
class SpeedDirectory(Enum):
    KM = 'км/ч'
    KN = 'узел'


@unique
class WeightDirectory(Enum):
    KG = 'кг'
    TN = 'т'


@unique
class StateDirectory(Enum):
    OK = 'готов'
    REPAIRING = 'ремонт'


@unique
class CitiesDirectory(Enum):
    MOSCOW = 'Москва'
    PETERBURG = 'Санкт-Петербург'
    NOVGOROD = 'Нижний Новгород'
    SAMARA = 'Самара'
    TUMEN = 'Тюмень'


@unique
class WeatherDirectory(Enum):
    RAIN = 'Дождь'
    SUNNY = 'Солнечно'
    CLOUDY = 'Облачно'
    STORM = 'Шторм'


@unique
class Color(Enum):
    RED = 'красный'
    WHITE = 'белый'
    GRAY = 'серый'


SPEED_DIRECTORY_PLURAL = {
    'KM': ('км/ч', 'км/ч', 'км/ч'),
    'KN': ('узел', 'узла', 'узлов')
}
