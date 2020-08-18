"""
Функция fib - расчет чисел Фибоначчи.
"""

from task1.decorators import trace


@trace
def fib(number, count=0):
    if number in [0, 1]:
        return number
    else:
        return fib(number - 1, count + 1) + fib(number - 2, count + 1)


# итератор последовательности чисел
def do_fib(limit):
    """
    :param limit: Сколько чисел вывести
    """
    result = []

    i = 0
    while i < limit:
        number = fib(i, 0)
        fib.count = 0

        result.append(number)
        i += 1

    return result
