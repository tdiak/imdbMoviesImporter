# -*- coding: utf-8

from flask_script import Manager
from app import app
from config import *
from importer.importer import DataImporter
from importer.aws_downloader import AwsDownloader


manager = Manager(app)


@manager.command
def get_imdb_files():
    AwsDownloader().get_all()


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
