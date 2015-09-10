#!/usr/bin/python3
#coding=utf-8

from flask import request, url_for, render_template, flash, g, session, redirect
from app import app, db
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from .forms import LoginForm, RegistrationForm
from .models import Role, User
from flask.ext.login import login_required, login_user, logout_user, current_user
from .email import send_mail

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    if current_user.is_authenticated() and not current_user.confirmed:
        print('\t ######## BEFORE REQUEST HANDLER', current_user.is_authenticated(), not current_user.confirmed)
        print(url_for('unconfirmed'))
        return redirect(url_for('unconfirmed'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated():
        session['known'] = True
    else:
        session['known'] = False
    return render_template('index.html', known=session.get('known', False))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('index'))
        flash('Неверные имя пользователя или пароль')
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('Спасибо, что зашли')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_mail(user.email, 'Подтвердите свой аккаунт', 'confirm', user=user, token=token)
        flash('Письмо с инструкциями для завершения успешной регистрации выслано на ваш email {0}'.format(user.email))
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('index'))
    if current_user.confirm(token):
        flash('Вы успешно подтвердили свой аккаунт. Спасибо!')
    else:
        flash('Проверочная сслыка неверна или истекло время ожидания.')
    return redirect(url_for('index'))

@app.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous() or current_user.confirmed:
        print('\t ######## UNCONFIRMED REDIRECT')
        print(current_user.is_anonymous(), current_user.confirmed)
        return redirect('index')
    return render_template('unconfirmed.html')

@app.route('/confirm')
@login_required
def resend_confirmation(token):
    token = current_user.generate_confirmation_token()
    send_mail(current_user.email, 'Подтвердите свой аккаунт', 'confirm', user=current_user, token=token)
    flash('Новое письмо с инструкциями для завершения успешной регистрации выслано на ваш email {0}'.format(current_user.email))
    return redirect(url_for('index'))