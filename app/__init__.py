# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# dev,test, prod
def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    # 'C:\\Users\\Admin\\PycharmProjects\\book_catalog\\config\\dev.py'
    app.config.from_pyfile(configuration)

    db.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    return app
