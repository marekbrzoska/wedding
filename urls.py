#-*- coding=utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

import base.urls
import gifts.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^gifts/', include(gifts.urls)),
    #url(r'^galery/$', 'galery.views.list', name='galery'),

    # admin and admin docs
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^photologue/', include('photologue.urls')),

    # This one needs to be last. Anything that was not routed, will be routed by the "base" application
    url('', include(base.urls)),
)

from django.conf import settings
if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

