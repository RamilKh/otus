import sys
from os import path
sys.path.append(path.abspath(path.curdir))

from app.application import application
from app.config import config


if __name__ == '__main__':
    application.run(
        host=config.SERVER['HOST'],
        port=config.SERVER['PORT'],
        debug=config.DEBUG,
        load_dotenv=True
    )
