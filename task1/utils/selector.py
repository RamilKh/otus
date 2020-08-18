"""
Функция selector - принимает на взод список из целых чисел, и возвращает
только чётные/нечётные/простые числа (выбор производится передачей
дополнительного аргумента)
"""


# возвращает четное ли число
def is_even(number):
    if number % 2 == 0:
        return True

    return False


# возвращает нечетное ли число
def is_odd(number):
    if number % 2 == 0:
        return False

    return True


# возвращает простое ли число - условие, что число не простые (1, четные)
def is_simple_waste(number):
    if number < 2:
        return False

    elif number == 2:
        return True

    elif is_odd(number) is True:
        return True

    return False


# возвращает простое ли число - расчет
def is_simple_run(number):
    result = True

    for i in range(2, number):
        if number % i == 0:
            result = False
            break

    return result


def selector(numbers, select=''):
    if select == 'even':
        return list(filter(is_even, numbers))

    elif select == 'odd':
        return list(filter(is_odd, numbers))

    elif select == 'simple':
        # отфильтровать числа, которые точно не простые (1 и четные)
        numbers = list(filter(is_simple_waste, numbers))

        # отфильтровать числа с расчетом
        return list(filter(is_simple_run, numbers))

    return []
