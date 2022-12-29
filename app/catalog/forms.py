from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField, IntegerField, FloatField, FileField
from wtforms.validators import DataRequired, ValidationError

from app.catalog.models import Publication, Book


class EditBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    num_pages = StringField('Pages', validators=[DataRequired()])
    submit = SubmitField('Update')

def image_exists(form,field):
    filename = secure_filename(form.img_file.data.filename)
    book = Book.query.filter_by(image=filename).first()

    if book:
        raise ValidationError('Image Already Exists')

def publisher_id_not_exist(form,field):
    id = Publication.query.filter_by(id=field.data).first()

    if not id:
        raise ValidationError('Publisher Doesnot exist Exists')
class CreateBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    avg_rating = FloatField('Rating', validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])

    img_file = FileField( validators=[DataRequired(), image_exists])
    num_pages = IntegerField('Pages', validators=[DataRequired()])
    pub_id = IntegerField('Publisher ID', validators=[DataRequired(),publisher_id_not_exist])
    submit = SubmitField('Create')

def publisher_exists(form,field):
    name = Publication.query.filter_by(name=field.data).first()

    if name:
        raise ValidationError('Publisher Already Exists')



class CreatePublisherForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), publisher_exists])
    id = IntegerField('Publisher ID', validators=[DataRequired()])
    submit = SubmitField('Create')