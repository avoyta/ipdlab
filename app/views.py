#!/usr/bin/python3
#coding=utf-8

from flask import request, url_for, render_template, flash, g, session, redirect
from app import app, db
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from .forms import NameForm, LoginForm
from .models import Role, User
from flask.ext.login import login_required

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))

@app.route('/login')
def login():
    return render_template('login.html', form=LoginForm())

@app.route('/secret')
@login_required
def secret():
    return "Only authenticated users are allowed!"