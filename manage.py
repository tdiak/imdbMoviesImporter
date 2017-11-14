from flask_script import Manager
from app import app
from config import *

manager = Manager(app)


@manager.command
def get_imdb_files():
    pass


@manager.command
def unpack_files():
    pass


@manager.command
def load_data():
    pass


@manager.command
def clean_data():
    pass


@manager.command
def runserver():
    app.run(host=APP_HOST, port=APP_PORT)


if __name__ == "__main__":
    manager.run()
