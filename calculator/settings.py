"""
Settings for application.
"""
import tempfile
db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = 'this really needs to be changed'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../flask-calculator.db'
