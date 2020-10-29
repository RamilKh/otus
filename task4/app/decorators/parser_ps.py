"""
Декоратор parer_ps - парсер результата вывода комманды docker ps.
"""

from functools import wraps


def parser_ps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        stdout = result['stdout']

        """
        stdout: строки разделены \n
        Шаблон строки "id = {{.ID}} | name = {{.Names}} | status = {{.Status}} | created = {{.CreatedAt}} | Port = {{.ports}}"
        """
        data = list()

        # Парсим построчно
        rows = stdout.split('\n')

        for row in rows:
            # Парсим свойства Id, Name, Status и т.д.
            properties = row.split(' | ')

            item = dict()
            for prop in properties:
                # Парсим значения 'ключ = значение' свойства
                values = prop.split(' = ')

                if len(values) == 2:
                    item[values[0]] = values[1]

            if len(item.keys()) > 0:
                data.append(item)

        result['data'] = data
        return result

    return wrapper
