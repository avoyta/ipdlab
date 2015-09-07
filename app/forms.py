#!/usr/bin/python3
#coding=utf-8

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('Как Вас зовут?', validators=[Required()])
    submit = SubmitField('Отправить')