from gino import Gino

DB = Gino()


class ExchangeRatesModel(DB.Model):
    """Курсы валют"""
    """Управление миграциими через alembic"""

    __tablename__ = 'exchange_rates'

    id = DB.Column(DB.Integer(), primary_key=True)
    name = DB.Column(DB.Unicode(), nullable=False)
    date = DB.Column(DB.String(), nullable=False)
    date_request = DB.Column(DB.String(), nullable=False)
    usd = DB.Column(DB.Float(precision=8), nullable=True)
    eur = DB.Column(DB.Float(precision=8), nullable=True)
    gbp = DB.Column(DB.Float(precision=8), nullable=False)

    def __str__(self):
        return f'Exchange rate: {self.name} to USD - {self.usd}, EUR - {self.eur}, GBP - {self.gbp} by {self.date_request}'

    __repr__ = __str__
