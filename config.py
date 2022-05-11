import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'ed96823c766c274dc3bd19e0'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'iansangthedev@gmail.com'
    MAIL_PASSWORD = 'Iansangthedev1!'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
