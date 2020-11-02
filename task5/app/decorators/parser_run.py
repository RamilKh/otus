"""
Декоратор parer_run - парсер результата вывода комманды docker run.
"""

from functools import wraps


def parser_run(func):
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
