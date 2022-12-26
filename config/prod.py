import os

DEBUG = False
SECRET_KEY='topsecert'
if os.getenv('DATABASE_URL'):
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL').replace("postgres://","postgresql://",1)
SQLALCHEMY_TRACK_MODIFICATIONS=False