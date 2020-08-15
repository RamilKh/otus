"""
Функция raise_power - принимает N целых чисел и возводит числа в степень
"""
from task1.decorators import timing


# возводит число number в степень power
def do_power(power=2):
    if power is None:
        power = 2

    def wrapper(number):
        return number ** power

    return wrapper


# принимает числа args и возвращает список чисел, возведенных в степень kwargs['power']
def raise_power(*args, **kwargs):
    power = kwargs.get('power')

    # итеративно применить функцию возведения в степень
    return list(map(
        do_power(power),
        args
    ))


@timing
def timer_raise_power(*args, **kwargs):
    return raise_power(*args, **kwargs)
