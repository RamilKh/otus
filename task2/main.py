from task2.classes import Ship, Aircraft, Car, AutoCar, BusCar, CargoAircraft, MilitaryShip
from task2.configs.const import Color, CitiesDirectory, WeatherDirectory
from task2.classesdata import Weather


if __name__ == '__main__':
    # ПРИМЕРЫ ВЫПОЛНЕНИЯ
    print()
    print('#####################################')
    print('1. Автомомобиль')
    car = Car(speed=100, color=Color.RED, name='Рабочий автомобиль Майка')
    print(car.__doc__)
    print(car)
    print()

    car.go(CitiesDirectory.SAMARA, CitiesDirectory.NOVGOROD)
    car.go(CitiesDirectory.MOSCOW, CitiesDirectory.PETERBURG)
    car.go(CitiesDirectory.MOSCOW, CitiesDirectory.TUMEN)
    car.refuel()
    car.go(CitiesDirectory.MOSCOW, CitiesDirectory.TUMEN, extreme=True)

    car.go(CitiesDirectory.PETERBURG, CitiesDirectory.TUMEN)
    car.repair()
    car.refuel()
    car.go(CitiesDirectory.PETERBURG, CitiesDirectory.TUMEN)

    ############################################
    print()
    print('#####################################')
    print('2. Корабль')
    ship = Ship(speed=100, fuel=130, name='Круизный лайнер BlueDream')
    print(ship.__doc__)
    print(ship)
    print()
    weather = Weather()
    weather.sunny()

    ship.go(CitiesDirectory.SAMARA, CitiesDirectory.NOVGOROD, weather.state)
    ship.refuel()

    weather.set_weather(WeatherDirectory.STORM)
    ship.go(CitiesDirectory.MOSCOW, CitiesDirectory.TUMEN, weather.state)

    weather.sunny()
    ship.go(CitiesDirectory.PETERBURG, CitiesDirectory.TUMEN)
    print()

    ############################################
    print()
    print('#####################################')
    print('3. Самолет')
    aircraft = Aircraft(speed=500, passengers=284, name='Пассажирский самолет Airbus 340')
    print(aircraft.__doc__)
    print(aircraft)
    print()

    aircraft.go(CitiesDirectory.SAMARA, CitiesDirectory.NOVGOROD,)
    aircraft.refuel()

    aircraft.go(CitiesDirectory.MOSCOW, CitiesDirectory.TUMEN)

    aircraft.go(CitiesDirectory.PETERBURG, CitiesDirectory.TUMEN)
    print()

    ############################################
    print()
    print('#####################################')
    print('4. Конкретные классы')
    autoCar = AutoCar(speed=150, color=Color.GRAY)
    print(autoCar.__doc__)
    print(autoCar)
    autoCar.start()
    autoCar.go(CitiesDirectory.MOSCOW, CitiesDirectory.TUMEN)

    autoCar.stop()
    autoCar.go(CitiesDirectory.PETERBURG, CitiesDirectory.TUMEN)

    busCar1 = BusCar(speed=100, color=Color.WHITE)
    busCar2 = BusCar(speed=100, color=Color.RED)
    print()
    print(busCar1.__doc__)
    print(busCar1)

    busCar1.go(CitiesDirectory.SAMARA, CitiesDirectory.NOVGOROD)
    position = busCar1.get_position()
    if position is not None:
        print(f'{busCar1.get_name()} сейчас в городе {position.value}')
    else:
        print(f'{busCar1.get_name()} еще никуда не выезжал')

    print()
    print(busCar2.__doc__)
    print(busCar2)
    position = busCar2.get_position()
    if position is not None:
        print(f'{busCar2.get_name()} сейчас в городе {position.value}')
    else:
        print(f'{busCar2.get_name()} еще никуда не выезжал')

    militaryShip = MilitaryShip(speed=20)
    print()
    print(militaryShip.__doc__)
    print(militaryShip)

    militaryShip.shoot_rocket(2)
    militaryShip.trace_enemy()
    militaryShip.shoot_rocket(9)
    militaryShip.stop_trace_enemy()

    cargoAircraft = CargoAircraft(speed=300, passengers=2)
    print()
    print(cargoAircraft.__doc__)
    print(cargoAircraft)

    cargoAircraft.set_products(['Мука', 'Кукуруза', 'Рис'])
    cargoAircraft.supply(CitiesDirectory.SAMARA, CitiesDirectory.NOVGOROD)

    cargoAircraft.supply(CitiesDirectory.MOSCOW, CitiesDirectory.PETERBURG)
