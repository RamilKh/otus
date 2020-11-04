from flask import Flask
from app.config import config
from app.view import admin_app, pages_app
from flask_migrate import Migrate
from app.models import db
from flask_login import LoginManager
from datetime import timedelta
from app.quiries.users import query_get

# application
application = Flask(__name__)
application.debug = True

# init settings
application.config.update(
    SQLALCHEMY_DATABASE_URI=f"postgresql+psycopg2://{config.DATABASE['USER']}:{config.DATABASE['PASSWORD']}@{config.DATABASE['HOST']}:5432/{config.DATABASE['NAME']}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SECRET_KEY=config.AUTH_SECRET_KEY,
    REMEMBER_COOKIE_HTTPONLY=True,
    PERMANENT_SESSION_LIFETIME=timedelta(days=config.AUTH_LIFETIME),
)
login_manager = LoginManager(application)
login_manager.session_protection = config.AUTH_PROTECTION
login_manager.login_view = "admin.login"


@login_manager.user_loader
def load_user(user_id):
    return query_get(user_id)


# init database
db.init_app(application)
migrate = Migrate(application, db)

# init routes
application.register_blueprint(admin_app)
application.register_blueprint(pages_app)
