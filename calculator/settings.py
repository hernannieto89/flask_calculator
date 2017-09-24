import tempfile
db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = 'aafeb9552c67474e9b6ce85f0394aab1'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../flask-calculator.db'
