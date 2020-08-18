"""
Декоратор trace - показывает вложенные входы в функцию.
"""

from functools import wraps


def trace(func):
    def get_space(number):
        space = ''
        index = 0;
        while index < number:
            space = space + '---'
            index += 1

        return space

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        count = wrapper.count

        func_name = func.__name__
        func_args = args
        space = get_space(count)

        if count == 1:
            print()
            print(f'{func_name}{func_args} run:')

        print(f'{space} -> {func_name}{func_args}')
        result = func(*args)
        print(f'{space} <- {func_name}{func_args} = {result}')

        return result

    wrapper.count = 0
    return wrapper
