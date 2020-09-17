from task3.classes import CollectorRate, Saver
from task3.utils.functions import get_last_days
import asyncio
from loguru import logger


def run():
    logger.info('Start parsing')

    # Получение курса валют
    collector = CollectorRate()
    saver = Saver()

    # сгенерировать последние n дней
    dates = get_last_days(7)

    # получить данные по дням и добавить в базу
    for date in dates:
        result = collector.get(date=date)
        if 'date' in result:
            # записать в базу дату получения курса (api может возвращать другую дату)
            result['date_request'] = date.strftime('%Y-%m-%d')

            # ищем есть ли запись в БД за текущую дату
            exists = asyncio.run(saver.get_by_date(result['date_request']))

            # записи нет - добавляем в базу
            if len(exists) == 0:
                logger.info(f'Created: {result}')
                asyncio.run(saver.create(result))
            else:
                logger.info(f'Exist: {result}')

    logger.info('Finish parsing')


def get():
    logger.info('')
    logger.info('Start view')
    saver = Saver()
    items = asyncio.run(saver.get_all())

    for item in items:
        logger.info(f'{item}')

    logger.info('Finish  view')


if __name__ == '__main__':
    # parsing ans saving in BD
    try:
        run()
    except Exception as error:
        logger.error(error)

    # view all records
    get()
