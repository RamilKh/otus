"""
Функция fib - расчет чисел Фибоначчи.
"""

from task1.decorators import trace


@trace
def fib(number):
    """
    fib.count: счетчик вложенности.
    В этой функии управляем счетчиком вложенности отсюда, так как логика подсчета вложенности
    в декораторе рассчитана на одиночную рекурсию, а здесь за раз вызываем два раза.
    """

    count = 0

    # если в декораторе count есть, берем оттуда
    if 'count' in fib.__dict__:
        is_count = True
        count = fib.count

    if number == 0 or number == 1:
        return 1
    else:
        number_1 = number-1
        number_2 = number-2

        result_1 = fib(number_1)

        # сохранить count, так как result_1 и result_2 на одном уровне
        fib.count = count

        result_2 = fib(number_2)

        # увеличить count
        fib.count += count

        return result_1 + result_2


# итератор последовательности чисел
def do_fib(limit):
    """
    :param limit: Сколько чисел вывести
    """
    result = []

    i = 0
    while i < limit:
        number = fib(i)
        fib.count = 0

        result.append(number)
        i += 1

    return result