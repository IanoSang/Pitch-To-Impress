from app import app
from flask import render_template, redirect, url_for, flash
from app.models import User
from app.forms import RegisterForm
from app import db
from flask_login import login_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/signUp', methods=['GET', 'POST'])
def signUp_page():
    form = RegisterForm()
    if form.validate_on_submit():
        use_to_create = User(username=form.username.data,
                             email_address=form.email_address.data, password=form.password1.data)
        db.session.add(use_to_create)
        db.session.commit()
        return redirect(url_for('login_page'))
    if form.errors != {}:  # If there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('signUp.html', form=form)
