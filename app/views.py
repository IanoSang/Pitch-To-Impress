from app import app
from flask import render_template
from app.models import User
from app import db


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


