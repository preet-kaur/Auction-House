# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Bids.models import Credits
from Browse.models import Items, Bought
from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
User = get_user_model()


def show_listings(request):
    active = 'showlist'
    all_items = Items.objects.all()
    items = all_items.filter(seller=User.objects.get(username=request.user.username))
    user_name = User.objects.get(username=request.user.username)
    credits = Credits.objects.get(name=user_name)
    score = credits.credit
    context = {
        'items': items,
        'score':score,
        'user_name': user_name,
    }

    return render(request, 'Bids/index.html', context, {'active':active})


def show_bids(request):
    active = 'showbid'
    all_items = Items.objects.all()
    items = all_items.filter(cur_highest_bidder=User.objects.get(username=request.user.username))
    print(items)
    user_name = User.objects.get(username=request.user.username)
    credits = Credits.objects.get(name=user_name)
    score = credits.credit
    context = {
        'items': items,
        'active':'showbid',
        'score':score,
        'user_name': user_name,
    }

    return render(request, 'Bids/index.html', context)


def show_bought(request):
    all_items = Bought.objects.all()
    items = all_items.filter(buyer=User.objects.get(username=request.user.username))
    print(items)
    user_name = User.objects.get(username=request.user.username)
    credits = Credits.objects.get(name=user_name)
    score = credits.credit
    context = {
        'items': items,
        'score':score,
        'user_name': user_name,
    }

    return render(request, 'Bids/index.html', context)


def details(request, item_id):
    cur_item = Items.objects.get(pk=item_id)
    user_name = User.objects.get(username=request.user.username)
    credits = Credits.objects.get(name=user_name)
    score = credits.credit
    context = {
        'cur_item': cur_item,
        'score':score,
        'user_name': user_name,
    }
    return render(request, 'Bids/details.html', context)