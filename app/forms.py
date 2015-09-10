#!/usr/bin/python3
#coding=utf-8

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from .models import User

class NameForm(Form):
    name = StringField('Как Вас зовут?', validators=[DataRequired()])
    submit = SubmitField('Отправить')

class LoginForm(Form):
    email = StringField('Адрес Email', validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Оставаться в системе')
    submit = SubmitField('Войти')
    
class RegistrationForm(Form):
    email = StringField('Адрес Email', validators=[DataRequired(), Length(1,64), Email()])
    username = StringField('Имя пользователя', validators=[DataRequired(),
                                                           Length(1,64),
                                                           Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                  'Имя пользователя может содержать только буквы, цифры, точку и знак подчеркивания')])
    password = PasswordField('Пароль', validators=[DataRequired(),
                                                   EqualTo('password2', message='Пароли должны совпадать')])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Такой адрес Email уже зарегистрирован')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Такой пользователь уже зарегистрирован')
