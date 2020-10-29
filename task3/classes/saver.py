from task3.configs.settings import DATABASES
from task3.models.models import ExchangeRatesModel, DB


class Saver:
    """Класс для сохранения данных в БД"""

    @classmethod
    async def connect(cls):
        settings = DATABASES['postgresql']
        await DB.set_bind(f"postgresql://{settings['USER']}:{settings['PASSWORD']}@{settings['HOST']}/{settings['NAME']}")

    @classmethod
    async def disconnect(cls):
        await DB.pop_bind().close()

    @classmethod
    async def get(cls, pk: int):
        await cls.connect()
        result = await ExchangeRatesModel.get(pk)
        await cls.disconnect()
        return result

    @classmethod
    async def get_by_date(cls, value):
        await cls.connect()
        result = await ExchangeRatesModel.query.where(
            ExchangeRatesModel.date_request == value,
        ).gino.all()
        await cls.disconnect()
        return result

    @classmethod
    async def get_all(cls):
        await cls.connect()
        result = await ExchangeRatesModel.query.gino.all()
        await cls.disconnect()
        return result

    @classmethod
    async def create(cls, data: dict):
        await cls.connect()
        result = await ExchangeRatesModel.create(
            name=data.get('base'),
            date=data.get('date'),
            date_request=data.get('date_request'),
            usd=data['rates'].get('USD'),
            eur=data['rates'].get('EUR'),
            gbp=data['rates'].get('GBP'),
        )
        await cls.disconnect()
        return result
