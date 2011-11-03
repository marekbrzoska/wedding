#-*- coding=utf-8 -*- 

from django import forms

from gifts.models import Gift

class ReserveGiftForm(forms.ModelForm):
    buyer = forms.CharField(max_length=200, label=u"Name")

    class Meta:
        model = Gift
        fields = ['buyer']
