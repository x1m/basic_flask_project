from flask import render_template
from app import app
from config import BASEDIR

@app.route('/')
def index():
    return render_template('index.html')
