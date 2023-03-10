# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login' # lets the login manager know which function we are using to log the user into the app
login_manager.session_protection = 'strong' # proctects user session (login,pass) - flask deletes session/cookies and forces the user to logout and login again to protect the sensitive data
bcrypt = Bcrypt()



# dev,test, prod

def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    # 'C:\\Users\\Admin\\PycharmProjects\\book_catalog\\config\\dev.py'
    app.config.from_pyfile(configuration)

    db.init_app(app)  # binds db to flask app
    bootstrap.init_app(app)  # initializes bootstrap
    login_manager.init_app(app)
    bcrypt.init_app(app)
    from app.catalog import main  # importing blueprint
    app.register_blueprint(main)  # registering the blueprint

    from app.auth import authentication as at  # importing blueprint
    app.register_blueprint(at)  # registering blueprint

    return app
