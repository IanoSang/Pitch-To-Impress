from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pitches.db'
app.config['SECRET_KEY'] = 'ed96823c766c274dc3bd19e0'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

db = SQLAlchemy(app)

from app import views
