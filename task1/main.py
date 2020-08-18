from task1.utils import do_fib, raise_power, timer_raise_power, selector, factorial
from enum import Enum, unique


if __name__ == '__main__':
    # ПРИМЕРЫ ВЫПОЛНЕНИЯ ФУНКЦИЙ

    print()
    print()
    print('#####################################')
    print('1. ФУНКЦИЯ ВОЗВЕДЕНИЯ ЧИСЛА В СТЕПЕНЬ')
    input_power = 2
    output = raise_power(1, 2, 3, 4, 5)
    print(f'Числа [1, 2, 3, 4, 5] в степень {input_power}:', output)

    input_power = 3
    output = raise_power(-8, 2.3, 35, 1.34, -5, 87, power=input_power)
    print(f'Числа [-8, 2.3, 35, 1.34, -5, 87] в степень {input_power}:', output)

    #####################################################################################
    print()
    print()
    print('#######################################################################')
    print('2. ДЕКОРАТОР ВРЕМЕНИ ВЫПОЛЕНИЯ ФУНКЦИИ НА ПРИМЕРЕ ВОЗВЕДЕНИЯ В СТЕПЕНЬ')

    input_power = 500000
    print(f'Расчет времени выполнения - возведение числа 4561 в степень {input_power}')
    output = timer_raise_power(4561, power=input_power)

    #####################################################################################
    print()
    print()
    print('###########################')
    print('3. ФУНКЦИЯ ФИЛЬТРАЦИИ ЧИСЕЛ')

    @unique
    class PowerSelectType(Enum):
        EVEN = 'even'
        ODD = 'odd'
        SIMPLE = 'simple'

    # 2. Функция возведения в степень
    input_numbers = [1, 2, 3, 4, 5, 11, 13, 14, 15, 17, 21, 22, 23, 25, 30, 31, 93, 97, 220, 251, 289, 769, 780, 820,
                     983, 985, 993, 997]
    print(f'Исходный список: {len(input_numbers)} элементов')
    print(input_numbers)
    print()

    output = selector(input_numbers, select=PowerSelectType.EVEN.value)
    print(f'Четные числа: {len(output)} элементов')
    print(output)
    print()

    output = selector(input_numbers, select=PowerSelectType.ODD.value)
    print(f'Нечетные числа: {len(output)} элементов')
    print(output)
    print()

    output = selector(input_numbers, select=PowerSelectType.SIMPLE.value)
    print(f'Простые числа: {len(output)} элементов')
    print(output)

    #####################################################################################
    print()
    print()
    print('#########################################################')
    print('4. ДЕКОРАТОР ВЛОЖЕННЫХ ФУНКЦИЙ НА ПРИМЕРЕ ЧИСЕЛ ФИБОНАЧЧИ')

    input_number = 10
    output = do_fib(input_number)
    print()
    print(f'Ряд чисел Фибоначчи до {input_number} ряда:', output)

    #####################################################################################
    print()
    print()
    print('####################################################')
    print('5. ДЕКОРАТОР ВЛОЖЕННЫХ ФУНКЦИЙ НА ПРИМЕРЕ ФАКТОРИАЛА')

    input_number = 10
    output = factorial(input_number)
    print()
    print(f'Факториал {input_number} равен', output)
