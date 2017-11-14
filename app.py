# -*- coding: utf-8

from flask import Flask

from models.db import db

app = Flask(__name__)

db.init_app(app)

app.config.from_object('config')

app.debug = app.config.get('DEBUG', False)
