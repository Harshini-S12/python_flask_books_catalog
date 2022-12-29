from flask_login import current_user, login_user, login_required
from werkzeug.utils import secure_filename

from app.auth.forms import LoginForm
from app.auth.models import User
from app.catalog import main
from app import db
from app.catalog.models import Book, Publication
from flask import render_template, flash, redirect, url_for, request
from app.catalog.forms import EditBookForm, CreateBookForm, CreatePublisherForm

ROWS_PER_PAGE = 6


# main -- blueprint
@main.route('/', methods=['GET', 'POST'])
def display_books():
    # Setting pagination configuration
    page = request.args.get('page', 1, type=int)

    books = Book.query.paginate(page=page, per_page=ROWS_PER_PAGE)  # Queries the database (calling class from models)
    return render_template('home.html', books=books)  # sending book object to Home.html file


@main.route('/display/publisher/<publisher_id>')
@login_required
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id=publisher.id).all()

    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)


@main.route('/book/delete/<book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash('Book deleted successfully')

        return redirect(url_for('main.display_books'))
    return render_template('delete_book.html', book=book, book_id=book_id)


@main.route('/edit/book/<book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = EditBookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.format = form.format.data
        book.num_pages = form.num_pages.data
        db.session.add(book)
        db.session.commit()
        flash('Edited Successfully ')
        return redirect(url_for('main.display_books'))
    return render_template('edit_book.html', form=form)


@main.route('/create/book/<pub_id>', methods=['GET', 'POST'])
@login_required
def create_book(pub_id):
    form = CreateBookForm()
    # form.pub_id.data = pub_id #prepopulates the pub_id

    if form.validate_on_submit():
        filename = secure_filename(form.img_file.data.filename)
        form.img_file.data.save('app/static/img/' + filename)
        book = Book(title=form.title.data, author=form.author.data, avg_rating=form.avg_rating.data,
                    book_format=form.format.data,
                    image=filename, num_pages=form.num_pages.data, pub_id=form.pub_id.data)
        db.session.add(book)
        db.session.commit()
        flash('Book Added Successfully')

        return redirect(url_for('main.display_publisher', publisher_id=form.pub_id.data))
    return render_template('create_book.html', form=form, pub_id=form.pub_id.data)


@main.route('/create/publisher/', methods=['GET', 'POST'])
@login_required
def create_publisher():
    form = CreatePublisherForm()

    if form.validate_on_submit():
        publisher = Publication(name=form.name.data)
        db.session.add(publisher)
        db.session.commit()
        flash('Publisher Added Successfully')

        return redirect(url_for('main.display_publisher', publisher_id=form.id.data))
    return render_template('createpublisher.html', form=form)
