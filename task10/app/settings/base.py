class BaseSettings:
    DEBUG = True

    # flask web server host
    SERVER = {
        'HOST': '127.0.0.1',
        'PORT': '9002',
    }

    # Lifetime authentication sessions (in days)
    AUTH_LIFETIME = 1
    AUTH_SECRET_KEY = '62h92jaks0k3'
    # none | basic | strong
    AUTH_PROTECTION = 'strong'

    # POSTGRES DATABASE
    DATABASE = {
        'HOST': '127.0.0.1',
        'NAME': 'otusds',
        'USER': 'otusds',
        'PASSWORD': 'otusds',
    }

    # Параметры докер peer-сервера
    PEER_SERVER = {
        'NAME_IMAGE': 'fastmeet-peer-server',
        'NAME_CONTAINTER': 'fastmeet-peer-server',
        'PORT': 9000
    }
