#create application object

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#connect app to SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mfiyzc.db'
db = SQLAlchemy(app)