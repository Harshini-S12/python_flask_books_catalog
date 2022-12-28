from app import create_app,db
from app.auth.models import User

flask_app = create_app('flask.cfg')
with flask_app.app_context():
    db.create_all()
    if not User.query.filter_by(user_name = 'harshini').first():
        User.create_user(user='harshini',email= 'harshinis@gmail.com',password='python')
flask_app.run()
