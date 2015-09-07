#!/usr/bin/python3
#coding=utf-8

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Email, Length

class NameForm(Form):
    name = StringField('Как Вас зовут?', validators=[Required()])
    submit = SubmitField('Отправить')

class LoginForm(Form):
    email = StringField('Адрес Email', validators=[Required(), Length(1,64), Email()])
    password = PasswordField('Пароль', validators=[Required()])
    remember_me = BooleanField('Оставаться в системе')
    submit = SubmitField('Войти')