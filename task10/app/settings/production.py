from .base import BaseSettings


class ProductionSettings(BaseSettings):
    DEBUG = False

    # flask web server host
    SERVER = {
        'HOST': '0.0.0.0',
        'PORT': '80',
    }

    # POSTGRES DATABASE
    DATABASE = {
        'HOST': 'otusdb',
        'NAME': 'otusapp',
        'USER': 'otusapp',
        'PASSWORD': 'otusapp',
    }
