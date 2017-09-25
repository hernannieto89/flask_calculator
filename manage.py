from flask_script import Manager
from flask_script.commands import ShowUrls, Clean
from calculator import create_app
from calculator.models import db

app = create_app('calculator.settings.Config')

manager = Manager(app)
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())

@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """

    db.create_all()

if __name__ == "__main__":
    manager.run()
