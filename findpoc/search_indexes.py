#!/usr/bin/python
# coding:utf-8
# another:blue-bird
from haystack import indexes
from .models import Links

class PocIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Links

