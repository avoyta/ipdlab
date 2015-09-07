#!/usr/bin/python3
#coding=utf-8
__author__ = 'Артем'

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db
from app.models import Role, User

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)



if __name__ == '__main__':
    manager.add_command("shell", Shell(make_context=make_shell_context))
    manager.add_command('db', MigrateCommand)
    manager.run()
