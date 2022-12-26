from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, FileField
from wtforms.validators import DataRequired


class EditBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    num_pages = StringField('Pages', validators=[DataRequired()])
    submit = SubmitField('Update')


class CreateBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    avg_rating = FloatField('Rating', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])

    img_file = FileField( validators=[DataRequired()])
    num_pages = IntegerField('Pages', validators=[DataRequired()])
    pub_id = IntegerField('Publisher ID', validators=[DataRequired()])
    submit = SubmitField('Create')