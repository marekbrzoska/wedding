#-*- coding=utf-8 -*- 

from django.contrib import admin

from gifts.models import Gift, Link



class LinkInline(admin.StackedInline):
    '''This class is to show Links inline (together with some other class)'''
    model = Link
    extra = 2

class GiftAdmin(admin.ModelAdmin):
    '''This adds Links to Gitf model page in admin'''
    inlines = [LinkInline]


#register GiftAdmin to represent Gift
admin.site.register(Gift, GiftAdmin)
