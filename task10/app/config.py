import os
from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv
from app.settings.base import BaseSettings
from app.settings.local import LocalSettings
from app.settings.production import ProductionSettings


# GET PARAMS FROM ENV FILE
env_file = join(dirname(__file__), '.env')
load_dotenv(env_file)

# get environ
env = os.environ.get('env', None)

# get configs by environ
if env is None:
    config = BaseSettings()
elif env == 'production':
    config = ProductionSettings()
elif env == 'local':
    config = LocalSettings()
else:
    raise ValueError("Environment name isn't specified")

# overide from env
DB_PASSWORD = getenv('DB_PASSWORD', None)
if DB_PASSWORD is not None:
    config.DATABASE['PASSWORD'] = DB_PASSWORD

DB_NAME = getenv('DB_NAME', None)
if DB_NAME is not None:
    config.DATABASE['NAME'] = DB_NAME

DB_USER = getenv('DB_USER', None)
if DB_USER is not None:
    config.DATABASE['USER'] = DB_USER
