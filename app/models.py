from app import db, login_manager
from app import bcrypt
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer())
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    bio = db.Column(db.String(255), nullable=True)
    pitches = db.relationship('Pitch', backref='user', lazy=True)
    comment = db.relationship('Comment', backref='user', lazy="dynamic")

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Pitch(db.Model):
    __tablename__ = 'pitchtable'
    pitch_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True)
    title = db.Column(db.String(100), index=True)
    content = db.Column(db.String(500), index=True)
    category_name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    comment = db.relationship('Comment', backref='pitch', lazy="dynamic")

    def save_pitch(self, pitch):
        ''' Save the pitches '''
        db.session.add(pitch)
        db.session.commit()

    def __repr__(self):
        return f"Pitch('{self.title}')"


class Comment(db.Model):
    __tablename__ = 'commenttable'
    comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(500), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitchtable.pitch_id"))

    def save_comment(self, comment):
        ''' Save the comment '''
        db.session.add(comment)
        db.session.commit()

    def __repr__(self):
        return f"Pitch('{self.comment}')"
