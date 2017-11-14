# -*- coding: utf-8

from sqlalchemy import Table
from sqlalchemy.orm import relationship

from db import db

TitleName = Table('TitleName', db.metadata,
                  db.Column('id', db.Integer, primary_key=True),
                  db.Column('titleId', db.Integer, db.ForeignKey('Titles.id')),
                  db.Column('nameId', db.Integer, db.ForeignKey('Names.id'))
                  )


class Title(db.Model):
    __tablename__ = 'Titles'

    id = db.Column(db.Integer, primary_key=True)
    tsv_id = db.Column(db.String(20))
    title_type = db.Column(db.String(50))
    primary_title = db.Column(db.String(500))
    original_title = db.Column(db.String(500))
    is_adult = db.Column(db.Boolean)
    start_year = db.Column(db.Integer, nullable=True)
    end_year = db.Column(db.Integer, nullable=True)
    runtime_minutes = db.Column(db.Integer, nullable=True)
    genres = db.Column(db.String(500))
    names = relationship('Name', secondary=TitleName, backref='Title')

    def __init__(self, tsv_id, title_type, primary_title, original_title, is_adult, start_year, end_year,
                 runtime_minutes, genres):
        self.tsv_id = tsv_id
        self.title_type = title_type
        self.primary_title = primary_title
        self.original_title = original_title
        self.is_adult = is_adult
        self.start_year = start_year
        self.end_year = end_year
        self.runtime_minutes = runtime_minutes
        self.genres = genres

    def row2dict(self, nested=False):
        obj = {
            'primary_title': self.primary_title,
            'start_year': self.start_year,
            'runtime_minutes': self.runtime_minutes,
            'genres': self.genres,
        }
        if nested:
            obj.update({'names': [name.row2dict() for name in self.names]})
        return obj


class Name(db.Model):
    __tablename__ = 'Names'
    id = db.Column(db.Integer, primary_key=True)
    tsv_id = db.Column(db.String(20))
    primary_name = db.Column(db.String(250))
    birth_year = db.Column(db.Integer, nullable=True)
    death_year = db.Column(db.Integer, nullable=True)
    primary_profession = db.Column(db.PickleType)
    titles = relationship('Title', secondary=TitleName, backref='Name')

    def __init__(self, tsv_id, primary_name, birth_year, death_year, primary_profession):
        self.tsv_id = tsv_id
        self.primary_name = primary_name
        self.birth_year = birth_year
        self.death_year = death_year
        self.primary_profession = primary_profession

    def row2dict(self, nested=False):
        obj = {
            'primary_name': self.primary_name,
            'birth_day': self.birth_year,
            'death_year': self.death_year,
            'primary_profession': self.primary_profession,
        }
        if nested:
            obj.update({'movies': [movie.row2dict() for movie in self.titles]})
        return obj


from app import app

with app.app_context():
    db.create_all()
