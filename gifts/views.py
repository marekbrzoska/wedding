#-*- coding=utf-8 -*- 

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden

from wedding.gifts.models import Gift
from wedding.gifts.forms import ReserveGiftForm



############################################################
# request handlers #########################################
############################################################


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
    if request.method == 'POST':
        return reserve_gift(request, gift_id)  
    else:
        return show_gift(request, gift_id)



############################################################
# worker functions, not accessible directly from urls ######
############################################################


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
        return HttpResponseForbidden("Ktoś inny już to kupuje...")

    form = ReserveGiftForm(request.POST)
    if form.is_valid():
        gift.buyer = form.cleaned_data['buyer']
        gift.save()
        return render(request, 'gifts/reserved.html', {'gift' : gift})
    else:
        return render(request, 'gifts/show.html', {'form' : form, 'gift' : gift})

