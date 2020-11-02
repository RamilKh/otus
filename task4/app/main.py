from app.application import application
from app.settings.local import SERVER


if __name__ == '__main__':
    application.run(
        host=SERVER['HOST'],
        port=SERVER['PORT'],
        debug=True,
        load_dotenv=True
    )
