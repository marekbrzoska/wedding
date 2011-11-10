#-*- coding=utf-8 -*- 

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'gifts.views.list', name='gifts'),
    url(r'^(\d+)$', 'gifts.views.show', name='gift'),
)
