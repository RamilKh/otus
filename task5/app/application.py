from flask import Flask
from app.view import admin_app, api_app, pages_app


# application
application = Flask(__name__)
application.debug = True

# init routes
application.register_blueprint(admin_app)
application.register_blueprint(api_app)
application.register_blueprint(pages_app)
