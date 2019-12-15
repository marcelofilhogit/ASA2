from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '558a4ce5b55839a7fe6bb23cbbb6c846'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# postgresql+psycopg2://postgres:494656@localhost/trabalho

db = SQLAlchemy(app)

from flaskblog import routes