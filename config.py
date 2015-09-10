#!/usr/bin/python3
#coding=utf-8

import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = 'development key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'data.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_SUBJECT_PREFIX = '[IPD Lab]'
MAIL_SENDER = 'IPD Lab Admin - <a.python.dev@gmail.com>'
IPDLAB_ADMIN = os.environ.get('IPDLAB_ADMIN')