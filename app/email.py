#!/usr/bin/python3
#coding=utf-8

from app import app, mail
from flask.ext.mail import Message
from flask import render_template
from threading import Thread

def send_mail(to, subject, template, **kwargs):
    msg = Message(
        app.config['MAIL_SUBJECT_PREFIX'] + subject,
        sender=app.config['MAIL_SENDER'],
        recipients=[to]
    )
    msg.text = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)