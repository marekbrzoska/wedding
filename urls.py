#-*- coding=utf-8 -*- 

from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wedding.views.home', name='home'),
    # url(r'^wedding/', include('wedding.foo.urls')),
    url(r'^$', 'gifts.views.home', name='home'),
    url(r'^gifts$', 'gifts.views.gifts', name='gifts'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
