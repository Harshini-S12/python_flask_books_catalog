from app.auth.forms import Registration, LoginForm
from app import db, login_manager
from flask_login import login_user, logout_user, login_required,current_user
from app.auth import authentication as at
from flask import render_template, request, flash, redirect, url_for,session
import time
from app.auth.models import User


@at.route('/register', methods=['GET', 'POST'])
def register_user():

    if current_user.is_authenticated:

        flash("You need to sign out first")
        session['flash_timeout'] = time.time()+ 1

        return redirect(url_for('main.display_books'))

    form = Registration()
    if form.validate_on_submit():  # checks if the request is post request also checks if the data is valid
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        flash('Registered Successfully !!')
        return redirect(url_for('authentication.do_the_login'))

    return render_template('registration.html', form=form)


@at.route('/login', methods=['GET', 'POST'])
def do_the_login():

    if current_user.is_authenticated:
        flash('You are already logged In !!')
        return redirect(url_for('main.display_books'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid Credentials, Please try again')
            return redirect(url_for('authentication.do_the_login'))
        login_user(user, form.stay_loggedIn.data)  # writes the user credentials to the session
        return redirect(url_for('main.display_books'))

    return render_template('login.html', form=form)

@at.route('/logout')
@login_required
def log_out_user():

    logout_user() # deletes the user data from the session
    return redirect(url_for('main.display_books'))


@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

# @at.route('/check flash')
# def check_flash():
#     if 'flash_timeout' in session and time.time() >session['flash_timeout']:
#
#         del session['flash_timeout']
#     else:
#         flash('This is flash msg')
#
#     return redirect(url_for('main.display_books'))




