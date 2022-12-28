from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, FileField
from wtforms.validators import DataRequired, ValidationError

from app.catalog.models import Publication


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

def publisher_exists(form,field):
    email = Publication.query.filter_by(name=field.data).first()

    if email:
        raise ValidationError('Publisher Already Exists')
class CreatePublisherForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), publisher_exists])
    id = IntegerField('Publisher ID', validators=[DataRequired()])
    submit = SubmitField('Create')