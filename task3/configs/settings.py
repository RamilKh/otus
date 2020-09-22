from os.path import join, dirname
from os import getenv
from dotenv import load_dotenv

# get params from env file
path_env = join(dirname(__file__), '.env')
load_dotenv(path_env)

# init settings
DATABASES = {
    'postgresql': {
        'HOST': 'localhost',
        'NAME': 'task3',
        'USER': 'otus',
        'PASSWORD': getenv('DB_PASSWORD'),
    }
}
