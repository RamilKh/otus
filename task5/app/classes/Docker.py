from subprocess import run, PIPE
from app.settings.local import PEER_SERVER
from app.decorators import parser_ps, parser_run, parser_stop, parser_start, parser_rm


class Docker:
    """
    Класс работы с докером
    """

    # параметры контейнера
    image = PEER_SERVER['NAME_IMAGE']
    container = PEER_SERVER['NAME_CONTAINTER']
    port = PEER_SERVER['PORT']

    def __init__(self, **kwargs):
        """
        :param image - докер образ
        :param container - докер контейнер
        :param port - порт, в котором работает peer-server
        """

        if kwargs.get('image') is not None:
            self.image = kwargs.get('image')
        elif kwargs.get('container') is not None:
            self.container = kwargs.get('container')
        elif kwargs.get('port') is not None:
            self.port = kwargs.get('port')

    # Получить идентификатор контейнера
    def get_container(self, **kwargs):
        """
        :param kwargs: port - порт контейнера, name - имя контейнера, id - id контейнера
        """

        if kwargs.get('port') is not None:
            return self.container + '-' + str(kwargs.get('port'))
        elif kwargs.get('name') is not None:
            return kwargs.get('name')
        elif kwargs.get('id') is not None:
            return kwargs.get('id')

        return None

    # Комманда docker ps
    @parser_ps
    def ps(self, port=0, id=0, filter=None):
        """
        :param filter - отфильтровать по имени
        """

        cmd = 'docker ps  -a'
        cmd += ' --format "id = {{.ID}} | name = {{.Names}} | status = {{.Status}} | created = {{.CreatedAt}} | port = {{.Ports}}"'

        if port != 0:
            cmd += f' --filter="name={self.container}-{port}"'
        elif id != 0:
            cmd += f' --filter="id={id}"'
        elif filter is not None:
            cmd += f' --filter="name={filter}"'

        std = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

        return {
            'returncode': std.returncode,
            'stdout': std.stdout,
            'data': None,
        }

    # Комманда docker run
    @parser_run
    def run(self, port):
        """
        :param port: порт, в котором запускается докер-контейнер
        """

        cmd = f'docker run --name {self.container}-{port} -p {port}:{self.port} -d {self.image}'
        std = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

        return {
            'returncode': std.returncode,
            'stdout': std.stdout,
            'data': None,
        }

    # Комманда docker start
    @parser_start
    def start(self, **kwargs):
        container = self.get_container(**kwargs)
        cmd = f'docker start {container}'
        std = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

        return {
            'returncode': std.returncode,
            'stdout': std.stdout,
            'data': None,
        }

    # Комманда docker stop
    @parser_stop
    def stop(self, **kwargs):
        container = self.get_container(**kwargs)
        cmd = f'docker stop {container}'
        std = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

        return {
            'returncode': std.returncode,
            'stdout': std.stdout,
            'data': None,
        }

    # Комманда docker rm
    @parser_rm
    def remove(self, **kwargs):
        # получить идентификатор контейнера
        container = self.get_container(**kwargs)

        cmd = f'docker rm {container}'
        std = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

        return {
            'returncode': std.returncode,
            'stdout': std.stdout,
            'data': None,
        }

