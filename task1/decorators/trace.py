"""
Декоратор trace - показывает вложенные входы в функцию.
"""

from functools import wraps


def trace(func):
    def get_space(number):
        space = ''
        index = 0
        while index < number:
            space = space + '---'
            index += 1

        return space

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__

        number = args[0]
        count = args[1]

        space = get_space(count)

        if count == 0:
            print()
            print(f'{func_name}({number}) run:')

        print(f'{space} -> {func_name}({number})')
        result = func(*args)
        print(f'{space} <- {func_name}({number}) = {result}')

        return result

    return wrapper
