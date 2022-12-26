from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired,Length,Email,ValidationError,EqualTo

from app.auth.models import User


def email_exists(form,field):
    email = User.query.filter_by(user_email=field.data).first()

    if email:
        raise ValidationError('Email Already Exists')
class Registration(FlaskForm):
    name = StringField('Name ', validators=[DataRequired(), Length(3,15, message='Name should be between 3-15 characters')])
    email = StringField('Email ID ', validators=[DataRequired(),Email(),email_exists])
    password = PasswordField('Password', validators=[DataRequired(), Length(5,message='Password must be atleast 5 characters long')])
    confirm = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password', message='Password does not match')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email ID ', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedIn = BooleanField('stay logged-in')
    submit = SubmitField('LogIn')
