#-*- coding=utf-8 -*- 
from django.shortcuts import render

from wedding.gifts.models import Gift


def home(request):
    return render(request, 'home.html')

def gifts(request):
    return render(request, 'gifts/list.html', {'gifts':Gift.objects.all()})
