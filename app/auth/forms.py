from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class Registration(FlaskForm):
    name = StringField('Name ')
    email = StringField('Email ID ')
    submit = SubmitField('Register')
