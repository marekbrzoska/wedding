#-*- coding=utf-8 -*- 

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def directions(request):
    return render(request, 'directions.html')
