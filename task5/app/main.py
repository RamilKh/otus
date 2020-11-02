import sys
from os import path
sys.path.append(path.abspath(path.curdir))

from app.application import application
from app.settings.local import SERVER, DEBUG


if __name__ == '__main__':
    application.run(
        host=SERVER['HOST'],
        port=SERVER['PORT'],
        debug=DEBUG,
        load_dotenv=True
    )
