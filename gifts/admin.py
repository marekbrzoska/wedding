#-*- coding=utf-8 -*- 

from django.contrib import admin

from gifts.models import Gift, Link

admin.site.register(Gift)
admin.site.register(Link)
