#!/usr/bin/python
# coding:utf-8
# another:blue-bird

from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'admin/(\d)/(\d)/audit/',views.audit,name='audit'),
    url(r'^$', views.index,name='index'),
    url(r'^upload/',views.upload,name='upload'),
    url(r'^poc/(\d)/',views.seepoc,name='poc'),
    url(r'^search/', include('haystack.urls')),
    # url(r'^test/',views.test,name='test')

]