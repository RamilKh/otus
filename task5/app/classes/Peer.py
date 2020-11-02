# from app.classes import Docker
from .Docker import Docker
from app.settings.local import PEER_SERVER


class Peer:
    """
    Класс работы с peer-сервером
    """

    # параметры контейнера
    container = PEER_SERVER['NAME_CONTAINTER']

    @classmethod
    def run(cls, port):
        docker = Docker()
        return docker.run(port)

    @classmethod
    def start(cls, port):
        docker = Docker()
        return docker.run(port)

    @classmethod
    def start_by_id(cls, id):
        docker = Docker()

        return docker.start(id=id)

    @classmethod
    def stop(cls, port):
        docker = Docker()

        return docker.stop(port=port)

    @classmethod
    def stop_by_id(cls, id):
        docker = Docker()

        return docker.stop(id=id)

    @classmethod
    def remove(cls, port):
        docker = Docker()

        return docker.remove(port=port)

    @classmethod
    def remove_by_id(cls, id):
        docker = Docker()

        return docker.remove(id=id)

    @classmethod
    def clear(cls, port):
        docker = Docker()

        stop = docker.stop(port=port)
        remove = docker.remove(port=port)

        return stop, remove

    @classmethod
    def clear_by_id(cls, id):
        docker = Docker()

        stop = docker.stop(id=id)
        remove = docker.remove(id=id)

        return stop, remove

    # получить инфу peer-сервера
    @classmethod
    def get(cls, port):
        docker = Docker()
        return docker.ps(port=port)

    @classmethod
    def get_by_id(cls, id):
        docker = Docker()
        return docker.ps(id=id)

    def get_all(self):
        docker = Docker()
        return docker.ps(filter=self.container)
