from app import db, login_manager
from app import bcrypt
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    profile = db.Column(db.String(), nullable=False, default='Add you profile Info')
    pitches = db.relationship('Pitch', backref='owned_user', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Pitch(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    category = db.Column(db.String(length=30), nullable=False, unique=True)
    title = db.Column(db.Integer(), nullable=False)
    author = db.Column(db.String(255))
    pitch_content = db.Column(db.String(length=1024), nullable=False, unique=True)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item{self.name}{self.description}'
