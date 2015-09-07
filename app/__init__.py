#coding=utf-8
#!/usr/bin/python3
__author__ = 'Артем'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


from app import views, models