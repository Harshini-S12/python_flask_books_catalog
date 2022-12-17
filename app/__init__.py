# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()


# dev,test, prod
def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    # 'C:\\Users\\Admin\\PycharmProjects\\book_catalog\\config\\dev.py'
    app.config.from_pyfile(configuration)

    db.init_app(app) # binds db to flask app
    bootstrap.init_app(app) # initializes bootstrap
    from app.catalog import main # importing blueprint
    app.register_blueprint(main) # registering the blueprint

    #from app.auth import authentication as at # importing blueprint
    #app.register_blueprint(at) #registering blueprint
    return app
