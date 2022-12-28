from sqlalchemy import exc

from app import create_app,db
from app.auth.models import User
from app.catalog.models import Book, Publication

flask_app = create_app('prod')
with flask_app.app_context():

    db.create_all()
    try:
        if not User.query.filter_by(user_name = 'harshini').first():
            User.create_user(user='harshini',email= 'harshinis@gmail.com',password='python')

    except exc.IntegrityError:
        flask_app.run()
