from .base import BaseSettings


class ProductionSettings(BaseSettings):
    DEBUG = False

    # POSTGRES DATABASE
    DATABASE = {
        'HOST': 'otusdb',
        'NAME': 'otus7',
        'USER': 'otus7',
        'PASSWORD': 'otus7',
    }
