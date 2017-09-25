"""
Settings for application.
"""

class Config(object):
    SECRET_KEY = 'aafeb9552c67474e9b6ce85f0394aab1'
    SESSION_COOKIE_SECURE = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../flask-calculator.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
