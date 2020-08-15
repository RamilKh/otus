"""
Декоратор timing - замеряет время выполнения функции.
"""

from time import time
from functools import wraps


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = time()

        # выполнить переданную функцию
        result = func(*args, **kwargs)

        # расчитать время выполнения функции
        time_end = time()
        time_result = time_end - time_start

        func_name = func.__name__
        print(f'Время выполнения функции {func_name}: {round(time_result, 2)} sec')
        return result

    return wrapper
