from .base import BaseSettings


class LocalSettings(BaseSettings):
    # POSTGRES DATABASE
    DATABASE = {
        'HOST': '192.168.0.190',
        'NAME': 'otus7',
        'USER': 'otus7',
        'PASSWORD': 'otus7',
    }
