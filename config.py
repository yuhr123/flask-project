import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = ''
DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'database.db')
DATABASE_CONNECT_OPTIONS = {}

del os
