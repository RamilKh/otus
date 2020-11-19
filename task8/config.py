import os
from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv
from settings.base import BaseSettings
from settings.local import LocalSettings
from settings.production import ProductionSettings


# GET PARAMS FROM ENV FILE
env_file = join(dirname(__file__), 'settings/database.env')
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

# override from env
POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD', None)
if POSTGRES_PASSWORD is not None:
    config.DATABASE['PASSWORD'] = POSTGRES_PASSWORD

POSTGRES_DB = getenv('POSTGRES_DB', None)
if POSTGRES_DB is not None:
    config.DATABASE['NAME'] = POSTGRES_DB

POSTGRES_USER = getenv('POSTGRES_USER', None)
if POSTGRES_USER is not None:
    config.DATABASE['USER'] = POSTGRES_USER
