#-*- coding=utf-8 -*- 

from django.conf.urls.defaults import patterns, url

import settings

urlpatterns = patterns('',
    url(r'^$', 'base.views.home', name='home'),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
