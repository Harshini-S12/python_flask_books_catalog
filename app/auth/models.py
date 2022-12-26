from datetime import datetime
from app import db, bcrypt, login_manager  # app/__init__.py
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    user_email = db.Column(db.String(60), unique=True, nullable=False, index=True)
    user_password = db.Column(db.String(80), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.now)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password,
                                          password)  # (1 arg hashed password from db, 2 arg password entered by the user)

    # class method belongs to a class but are not associated with any class instance
    @classmethod
    def create_user(cls, user, email, password):
        user = cls(user_name=user, user_email=email,
                   user_password=bcrypt.generate_password_hash(password).decode('utf-8')  # python 3
                   )

        db.session.add(user)
        db.session.commit()

        return user


@login_manager.user_loader
def load_user(id):  # takes user_id in unicode format
    return User.query.get(int(id))  # need to return in integer because this function by default returns it as unicode
