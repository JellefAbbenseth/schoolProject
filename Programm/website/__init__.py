from flask import Flask
from flask_login import LoginManager
from os import path

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.testing.pickleable import User

from Programm.database import Database

# Erstellen der Verbindung von Webseite zu python mithilfe von Flask
# Verbinden Datenbank

db = SQLAlchemy()
DB_Name = 'schoolProject.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jkDSDU4723%/(9sdf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///Programm.database{DB_Name}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('datenbank/' + DB_Name):
        db.createTables(app=app)
        print('Created Database!')
