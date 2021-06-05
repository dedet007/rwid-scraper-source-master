import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# instantiate the extensions
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app(script_info=None):
    from project.models import models
    from project.admin.views import admin_blueprint
    from project.home.views import home_blueprint

    # instantiate the app
    app = Flask(__name__, static_url_path='')

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Setting up flask login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "admin.login"
    @login_manager.user_loader
    def load_user(user_id):
        return models.User.query.filter(models.User.id == int(user_id)).first()

    # register the blueprints
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(home_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
