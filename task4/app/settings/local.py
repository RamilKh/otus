from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv

# GET PARAMS FROM ENV FILE
env_file = join(dirname(__file__), '.env')
load_dotenv(env_file)

# SERVER
SERVER = {
    'HOST': getenv('HOST'),
    'PORT': getenv('PORT'),
}

# Параметры докер peer-сервера
PEER_SERVER = {
    'NAME_IMAGE': 'fastmeet-peer-server',
    'NAME_CONTAINTER': 'fastmeet-peer-server',
    'PORT': 9000
}
