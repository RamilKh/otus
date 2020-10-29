from task3.classes import CollectorABC
import asyncio
from asyncio import CancelledError
from aiohttp import ClientSession, ClientConnectorError
from loguru import logger


class Collector(CollectorABC):
    """Базовый класс для получения данных из открытого api"""

    REQUEST_DELAY = 1
    SERVICES = None

    def __init__(self, *args, **kwargs):
        if 'services' in kwargs:
            self.SERVICES = kwargs.get('services')

    def __enter__(self, **kwargs):
        self.__init__(**kwargs)
        return self.get(**kwargs)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    async def request(self, session, url, **kwargs) -> dict:
        await asyncio.sleep(self.REQUEST_DELAY)  # заглужка чтобы не заблокировали из-за частых запросов
        async with session.get(url) as response:
            return await response.json()

    async def fetch(self, url, **kwargs) -> dict:
        loop = asyncio.get_event_loop()

        try:
            async with ClientSession() as session:
                return await self.request(session, url, **kwargs)

        except ClientConnectorError as error:
            logger.info(error)
        except CancelledError:
            loop.stop()
        except Exception as error:
            logger.info(f'Ошибка: {error}')

    async def run(self, **kwargs):
        if self.SERVICES is None:
            raise ValueError('Укажите сервис данных (источник получения данных)')

        # create and run coroutines
        coroutines = [self.fetch(**kwargs, url=service.value) for service in list(self.SERVICES)]
        done, pending = await asyncio.wait(
            coroutines,
            timeout=3,
            return_when=asyncio.FIRST_COMPLETED
        )

        # cancel the pending coroutines
        for p in pending:
            p.cancel()

        # get result from async coroutines
        data = dict()
        for task in done:
            result = task.result()
            if result is not None:
                data = task.result()
                break

        return data

    def get(self, **kwargs):
        try:
            return asyncio.run(self.run(**kwargs))
        except ValueError as error:
            logger.error(error)
            return []
