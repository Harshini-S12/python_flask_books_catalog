from app.auth.forms import Registration
from app import db
from app.auth import authentication as at
from flask import render_template, request


@at.route('/register', methods=['GET', 'POST'])
def register_user():
    name = None
    email = None

    form = Registration()
    if request.method == 'POST':
        name = form.name.data
        email = form.email.data

    return render_template('registration.html', form=form, name=name, email=email)
