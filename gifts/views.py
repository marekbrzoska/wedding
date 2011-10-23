#-*- coding=utf-8 -*- 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse

from wedding.gifts.models import Gift
from wedding.gifts.forms import ReserveGiftForm


def home(request):
    return render(request, 'home.html')

def list(request):
    gifts = Gift.objects.all()
    for gift in gifts:
        gift.is_reserved = True if gift.buyer else False
            
    return render(
            request, 
            'gifts/list.html', 
            {
                'gifts' : gifts,
            }
            )

def show(request, gift_id):
    gift = get_object_or_404(Gift, id=gift_id)
    if gift.buyer:
        return HttpResponseForbidden()
    form = ReserveGiftForm()

    return render(
            request,
            'gifts/show.html',
            {
                'gift' : gift,
                'form' : form,
            }
            )

def reserve(request, gift_id):
    if request.method != 'POST':
        return HttpResponseForbidden("lal")

    gift = get_object_or_404(Gift, id=gift_id)
    if gift.buyer:
        return HttpResponseForbidden("Somebody has already declared buying this present!")

    form = ReserveGiftForm(request.POST)
    if form.is_valid():
        print '#'*80
        print form.cleaned_data['buyer']
        print '#'*80
        gift.buyer = form['buyer']
        gift.save()
        return HttpResponse("win")
    return HttpResponse("lose")

