from .application import app
from flask import render_template, url_for

@app.route('/')
def home():
    print(app.config['API_LIST'])
    return render_template('home.html')

