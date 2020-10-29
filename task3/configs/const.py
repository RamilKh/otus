from enum import Enum, unique


@unique
class ServiceRates(Enum):
    RATE1 = 'https://api.ratesapi.io/api/{0}?base=RUB&symbols=USD,EUR,GBP'
    RATE2 = 'https://api.exchangeratesapi.io/{0}?base=RUB&symbols=USD,EUR,GBP'
