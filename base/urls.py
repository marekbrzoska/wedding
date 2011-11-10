#-*- coding=utf-8 -*- 

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'base.views.home', name='home'),
)
