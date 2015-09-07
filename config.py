#!/usr/bin/python3
#coding=utf-8

import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = 'development key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'data.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
