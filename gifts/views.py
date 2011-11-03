#-*- coding=utf-8 -*- 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from wedding.gifts.models import Gift
from wedding.gifts.forms import ReserveGiftForm


def home(request):
    return render(request, 'home.html')

def list(request):
    gifts = Gift.objects.order_by('id')
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
    return reserve_gift(request, gift_id) if request.method == 'POST' else show_gift(request, gift_id)

def show_gift(request, gift_id):
    gift = get_object_or_404(Gift, id=gift_id)
    form = ReserveGiftForm() if not gift.buyer else None

    return render(
            request,
            'gifts/show.html',
            {
                'gift' : gift,
                'form' : form,
            }
            )

def reserve_gift(request, gift_id):
    gift = get_object_or_404(Gift, id=gift_id)
    if gift.buyer:
        return HttpResponseForbidden("Somebody has already declared buying this present!")

    form = ReserveGiftForm(request.POST)
    if form.is_valid():
        gift.buyer = form.cleaned_data['buyer']
        gift.save()
        return render(request, 'gifts/reserved.html', {'gift' : gift})
    else:
        return render(request, 'gifts/show.html', {'form' : form, 'gift' : gift})

