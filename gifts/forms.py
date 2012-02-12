#-*- coding=utf-8 -*- 

from django import forms

from gifts.models import Gift

class ReserveGiftForm(forms.ModelForm):
    buyer = forms.CharField(max_length=200, label=u"Kto (imię i nazwisko)")
    notice = forms.CharField(max_length=300, label=u"Kontakt (telefon/email)", required=False)

    class Meta:
        model = Gift
        fields = ['buyer', 'notice']
