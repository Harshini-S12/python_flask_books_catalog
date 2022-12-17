from app.catalog import main
from app import db
from app.catalog.models import Book, Publication
from flask import render_template


# main -- blueprint
@main.route('/')
def display_books():
    books = Book.query.all()  # Queries the database (calling class from models)
    return render_template('home.html', books = books) # sending book object to Home.html file
