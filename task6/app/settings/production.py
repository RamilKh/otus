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
        'HOST': '192.168.43.211',
        'NAME': 'otusapp',
        'USER': 'otusapp',
        'PASSWORD': 'otusapp',
    }
