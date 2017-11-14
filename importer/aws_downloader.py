# -*- coding: utf-8
import os

import boto3

from config import BASE_DIR


class AwsDownloader(object):
    def __init__(self, bucket_name='imdb-datasets'):
        self.key = None
        self.bucket_name = bucket_name
        self.s3 = s3 = boto3.resource('s3')

    def __get_file(self, filename, path=None):
        if not path:
            path = os.path.join(BASE_DIR, 'data', filename)
        self.s3.download_file(self.bucket_name, self.key, path)

    def get_names(self):
        self.key = 'documents/v1/current/names.basics.tsv.gz'
        self.__get_file(filename='name.basics.tsv.gz')

    def get_title(self):
        self.key = 'documents/v1/current/title.basics.tsv.gz'
        self.__get_file(filename='title.basics.tsv.gz')

    def get_all(self):
        self.get_names()
        self.get_title()