import os
import gzip
import csv

from config import BASE_DIR


class DataImporter(object):
    name_path = os.path.join(BASE_DIR, 'data', 'name.basics.tsv.gz')
    title_path = os.path.join(BASE_DIR, 'data', 'title.basics.tsv.gz')

    def __init__(self):
        pass

    def get_titles(self):
        i = 0
        with gzip.open(self.title_path, 'rb') as file:
            tsvreader = csv.reader(file, delimiter="\t")
            # example line
            # ['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes', 'genres']
            # ['tt0000003', 'short', 'Pauvre Pierrot', 'Pauvre Pierrot', '0', '1892', '\\N', '4', 'Animation,Comedy,Romance']
            for line in tsvreader:
                break

    def get_names(self):
        i=0
        with gzip.open(self.name_path, 'rb') as file:
            tsvreader = csv.reader(file, delimiter="\t")
            # example line
            # ['nconst', 'primaryName', 'birthYear', 'deathYear', 'primaryProfession', 'knownForTitles']
            # ['nm0000001', 'Fred Astaire', '1899', '1987', 'soundtrack,actor,miscellaneous', 'tt0120689,tt0028333,tt0050419,tt0027125']
            for line in tsvreader:
                break