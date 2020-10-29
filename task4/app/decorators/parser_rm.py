"""
Декоратор parser_rm - парсер результата вывода комманды docker rm.
"""

from functools import wraps


def parser_rm(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        stdout = result['stdout']

        """
        stdout: строки разделены \n
        """

        data = stdout.split('\n')
        result['data'] = data[0]

        return result

    return wrapper
