#coding=utf-8
#!/usr/bin/python3
__author__ = 'Артем'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views

from app import models