#-*- coding=utf-8 -*- 

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

import base.urls
import gifts.urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^gifts/', include(gifts.urls)),

    # admin and admin docs
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # This one needs to be last. Anything that was not routed, will be routed by the "base" application
    url('', include(base.urls)),
)
