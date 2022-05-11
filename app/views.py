from app import app
from flask import render_template, redirect, url_for, flash, abort
from app.models import User, Pitch, Comment
from app.forms import RegisterForm, LoginForm, UpdateProfile, AddPitchForm, CommentForm
from app import db, photos
from flask_login import login_user, login_required, logout_user, current_user
import urllib.request as urllib
from .email import mail_message


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/pitches')
@login_required
def pitches_page():
    pitches = Pitch.query.all()
    return render_template('pitches.html', pitches=pitches)


@app.route('/signUp', methods=['GET', 'POST'])
def signUp_page():
    form = RegisterForm()
    if form.validate_on_submit():
        use_to_create = User(username=form.username.data,
                             email_address=form.email_address.data, password=form.password1.data)
        db.session.add(use_to_create)
        db.session.commit()
        mail_message("Welcome to watchlist", "email/welcome_user", use_to_create.email_address,
                     use_to_create=use_to_create)

        return redirect(url_for('login_page'))
    if form.errors != {}:  # If there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('signUp.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Logged in Successfully! You logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('profile_page'))
        else:
            flash('Invalid Username or Password!! Please try again', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout_page():
    logout_user()
    flash('You have logged Out', category='info')
    return redirect(url_for("home_page"))


@app.route('/user/')
def profile_page():
    user = User.query.filter_by().first()

    if user is None:
        abort(404)

    return render_template("profile.html", user=user)


@app.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('update.html', form=form)


@app.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in urllib.files:
        filename = photos.save(urllib.files['photos'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('profile'))


@app.route('/comment', methods=['GET', 'POST'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment=comment, user_id=user_id, pitch_id=pitch_id)
        new_comment.save_c()
        return redirect(url_for('comment', pitch_id=pitch_id))
    form = CommentForm()
    return render_template('comment.html', form=form, pitch=pitch, all_comments=all_comments)


@app.route('/addpitch', methods=['GET', 'POST'])
def addpitch_page():
    form = AddPitchForm()
    if form.validate_on_submit():
        pitch = Pitch(email=form.email.data, title=form.title.data, content=form.content.data,
                      category_name=form.category_name.data)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been add success')
        return redirect(url_for('pitches_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error in creating the pitch:(err_msg)')

    return render_template('addPitch.html', form=form)
