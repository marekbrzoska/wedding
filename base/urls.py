#-*- coding=utf-8 -*- 

from django.conf.urls.defaults import patterns, url

import settings

urlpatterns = patterns('',
    url(r'^$', 'base.views.home', name='home'),
    url(r'^directions$', 'base.views.directions', name='directions'),
    url(r'^about$', 'base.views.about', name='about'),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
