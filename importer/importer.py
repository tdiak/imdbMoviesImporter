import os
import gzip
import csv

from config import BASE_DIR
from models.models import Title, Name
from models.db import db


class DataImporter(object):
    name_path = os.path.join(BASE_DIR, 'data', 'name.basics.tsv.gz')
    title_path = os.path.join(BASE_DIR, 'data', 'title.basics.tsv.gz')

    def import_titles(self):
        with gzip.open(self.title_path, 'rb') as file:
            tsvreader = csv.reader(file, delimiter="\t")
            # example line
            # ['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes', 'genres']
            # ['tt0000003', 'short', 'Pauvre Pierrot', 'Pauvre Pierrot', '0', '1892', '\\N', '4', 'Animation,Comedy,Romance']
            for i, line in enumerate(tsvreader):
                if i == 0:
                    continue
                title = Title(
                    tsv_id=line[0],
                    title_type=line[1],
                    primary_title=line[2],
                    original_title=line[3],
                    is_adult=line[4],
                    start_year=int(line[5]) if line[5] != '\\N' else None,
                    end_year=int(line[6]) if line[6] != '\\N' else None,
                    runtime_minutes=int(line[7]) if line[7] != '\\N' else None,
                    genres=line[8]
                )
                db.session.add(title)
                db.session.commit()

    def import_names(self):
        with gzip.open(self.name_path, 'rb') as file:
            tsvreader = csv.reader(file, delimiter="\t")
            # example line
            # ['nconst', 'primaryName', 'birthYear', 'deathYear', 'primaryProfession', 'knownForTitles']
            # ['nm0000001', 'Fred Astaire', '1899', '1987', 'soundtrack,actor,miscellaneous', 'tt0120689,tt0028333,tt0050419,tt0027125']
            for i, line in enumerate(tsvreader):
                if i == 0:
                    continue

                name = Name(
                    tsv_id=line[0],
                    primary_name=line[1],
                    birth_year=int(line[2]) if line[2] != '\\N' else None,
                    death_year=int(line[3]) if line[3] != '\\N' else None,
                    primary_profession=line[4]
                )

                db.session.add(name)
                db.session.commit()
                for id in line[5].split(','):
                    title = Title.query.filter(Title.tsv_id == id)
                    if title.count():
                        title = title[0]
                        title.names.append(name)
                        db.session.commit()
