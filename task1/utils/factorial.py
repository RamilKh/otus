"""
Функция factorial - рассчитывает факториал числа
"""

from task1.decorators import trace


@trace
def factorial(number):
    if number <= 0:
        return 1
    return number * factorial(number - 1)
