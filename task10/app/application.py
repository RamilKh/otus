from flask import Flask
from app.config import config
from app.view import admin_app, pages_app
from flask_migrate import Migrate
from app.models import db

# application
application = Flask(__name__)
application.debug = True

# init settings
application.config.update(
    SQLALCHEMY_DATABASE_URI=f"postgresql+psycopg2://{config.DATABASE['USER']}:{config.DATABASE['PASSWORD']}@{config.DATABASE['HOST']}:5432/{config.DATABASE['NAME']}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)


# init database
db.init_app(application)
migrate = Migrate(application, db)

# init routes
application.register_blueprint(admin_app)
application.register_blueprint(pages_app)
