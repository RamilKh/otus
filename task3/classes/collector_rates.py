import asyncio
from aiohttp import ClientSession
from task3.classes import Collector
from task3.configs.const import ServiceRates


class CollectorRate(Collector):
    """Класс для получения курсов валют"""

    REQUEST_DELAY = 0.5
    SERVICES = ServiceRates

    async def request(self, session: ClientSession, url: str, **kwargs) -> dict:
        date = kwargs.get('date')
        await asyncio.sleep(self.REQUEST_DELAY)  # заглужка чтобы не заблокировали из-за частых запросов
        async with session.get(url.format(date)) as response:
            return await response.json()
