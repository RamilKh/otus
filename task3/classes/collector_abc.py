from abc import ABCMeta, abstractmethod


class CollectorABC(metaclass=ABCMeta):
    """Абстрактный класс для базового класса для получения данных из открытого api"""

    # получение и опработка данных с запроса
    @abstractmethod
    def fetch(self):
        raise NotImplementedError

    # запуск получения данных
    @abstractmethod
    def run(self):
        raise NotImplementedError

    # http-запрос на получение данных
    @abstractmethod
    def request(self):
        raise NotImplementedError

    # для иницированя получения данных(формирования данных и последующего запуска)
    @abstractmethod
    def get(self):
        raise NotImplementedError
