# -*- coding: utf-8

from flask import Flask, jsonify, request

from models.db import db

app = Flask(__name__)

db.init_app(app)

app.config.from_object('config')

app.debug = app.config.get('DEBUG', False)

from models.models import Title, Name
from config import PAGE_SIZE


@app.route('/movies/<int:page>/')
def get_movies(page=1):
    movies = Title.query.order_by(Title.primary_title)

    if request.args.get('startYear'):
        movies = movies.filter(Title.start_year == int(request.args.get('startYear')))

    if request.args.get('genres'):
        movies = movies.filter(Title.genres.contains(request.args.get('genres')))

    movies = movies.paginate(page, PAGE_SIZE, error_out=False).items
    return jsonify({'movies': [movie.row2dict(nested=True) for movie in movies]})


@app.route('/names/<int:page>/')
def get_names(page=1):
    names = Name.query.order_by(Name.primary_name).filter(Name.titles.any())

    if request.args.get('primary_name'):
        names = names.filter(Name.primary_name.contains(request.args.get('primary_name')))

    names = names.paginate(page, PAGE_SIZE, error_out=False).items
    return jsonify({'names': [name.row2dict(nested=True) for name in names]})
