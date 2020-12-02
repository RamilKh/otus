from .base import BaseSettings


class LocalSettings(BaseSettings):
    # flask web server host
    SERVER = {
        'HOST': '0.0.0.0',
        'PORT': '80',
    }

    # POSTGRES DATABASE
    DATABASE = {
        'HOST': '192.168.43.211',
        'NAME': 'otusds',
        'USER': 'otusds',
        'PASSWORD': 'otusds',
    }
