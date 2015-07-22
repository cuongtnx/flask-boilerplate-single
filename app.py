from flask import Flask
from flask import flash, request, render_template, redirect, url_for

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


app = Flask(__name__)

UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Database connection:
# engine = create_engine('sqlite:///database.db')
# Base.metadata.bine = engine

# DBSession = sessionmaker(bind=engine)
# session = DBSession()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/pic/')
def pic():
    return render_template("picture.html")

@app.route('/form/', methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")

    return "Form submited"

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)


