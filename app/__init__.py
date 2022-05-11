from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pitches.db'
app.config['SECRET_KEY'] = 'ed96823c766c274dc3bd19e0'
app.config['UPLOADED_PHOTOS_DEST'] = 'app/static/photos'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
photos = UploadSet('photos', IMAGES)
# configure UploadSet
configure_uploads(app, photos)

mail = Mail()
mail.init_app(app)

db = SQLAlchemy(app)

from app import views
