from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import SECRET_KEY, DATABASE_URI

# initialize database
db = SQLAlchemy()

# initialize login manager
login_manager = LoginManager()


def create_app():
    """Construct the core app object"""
    app = Flask(__name__)

    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

    # initialize plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():

        from .views import views
        from .auth import auth

        # register blueprints
        app.register_blueprint(views, url_prefix='/')
        app.register_blueprint(auth, url_prefix='/')

        # create database models
        db.create_all()

        return app
