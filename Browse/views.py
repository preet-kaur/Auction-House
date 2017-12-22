# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date, datetime
from time import localtime

from django.utils import timezone
from django.conf import settings
from .models import Items, Expired, Bought
from Bids.models import Credits
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail,EmailMessage
from django.http import HttpResponse
# Create your views here.

User = get_user_model()

def show(request):
    if request.user.is_authenticated:
        exp = Expired()
        bt = Bought()
        for i in Items.objects.all():
            if i.cur_highest_bid!=0 and i.expiration < timezone.now():
                item = Items.objects.get(pk=i.item_id)
                bt.seller = item.seller
                bt.item_id = item.item_id
                bt.item_logo = item.item_logo
                bt.item_name = item.item_name
                bt.item_desc = item.item_desc
                bt.buyer = item.cur_highest_bidder
                bt.cur_highest_bid = item.cur_highest_bid
                bt.created_on = item.created_on
                bt.expiration = item.expiration
                bt.min_price = item.min_price
                bt.buy_now_price = item.buy_now_price
                bt.save()
                exp.seller = item.seller
                exp.item_id = item.item_id
                exp.item_name = item.item_name
                exp.item_desc = item.item_desc
                exp.created_on = item.created_on
                exp.min_price = item.min_price
                exp.buy_now_price = item.buy_now_price
                exp.save()
                item.delete()

            elif i.expiration < timezone.now():
                item = Items.objects.get(pk=i.item_id)
                exp.seller = item.seller
                exp.item_id = item.item_id
                exp.item_name = item.item_name
                exp.item_desc = item.item_desc
                exp.created_on = item.created_on
                exp.min_price = item.min_price
                exp.buy_now_price = item.buy_now_price
                exp.save()
                item.delete()

            #elif i.cur_highest_bid == i.buy_now_price:
             #   i.delete()

        all_items_list = Items.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(all_items_list, 8)
        try:
            all_items = paginator.page(page)
        except PageNotAnInteger:
            all_items = paginator.page(1)
        except EmptyPage:
            all_items = paginator.page(paginator.num_pages)
        user_name = User.objects.get(username=request.user.username)
        credits = Credits.objects.get(name=user_name)
        score = credits.credit
        context = {
            'all_items': all_items,
            'score':score,
            'user_name':user_name,
        }
        return render(request, 'Browse/index.html', context)
    else:
        return redirect('login:login')


def details(request, item_id):
    cur_item = Items.objects.get(pk=item_id)
    user_name = User.objects.get(username=request.user.username)
    credits = Credits.objects.get(name=user_name)
    score = credits.credit
    context = {
        'cur_item': cur_item,
        'score':score,
    }
    return render(request, 'Browse/details.html', context)


def update(request, item_id):
    all_items = Items.objects.all()
    cur_item = Items.objects.get(pk=item_id)
    user_name = User.objects.get(username=request.user.username)
    print(user_name)
    credits = Credits.objects.get(name=user_name)
    c1 = Credits.objects.get(name=cur_item.seller)
    score = credits.credit
    # print(credits)
    bid = request.POST['bid_value']
    if int(score) >= int(bid):
        html_content = "<strong>Your current bid has been overtaken by someone.</strong>"
        email = EmailMessage('Auction House:Sad news', html_content, to=['jainamsoni33@gmail.com'])
        email.content_subtype = "html"
        email.send()
        if int(bid) in range(int(cur_item.cur_highest_bid), int(cur_item.buy_now_price)) and int(bid) > cur_item.min_price:

            cur_item.cur_highest_bid = bid
            cur_item.cur_highest_bidder = User.objects.get(username=request.user.username)
            cur_item.save()
            #credits.credit = int(credits.credit) - int(bid)
            #credits.save()
            #c1.credit = int(c1.credit) + int(bid)
            #c1.save()

            context = {
                'all_items': all_items,
            }
            return render(request, 'Browse/index.html', context)
        elif int(bid) >= int(cur_item.buy_now_price):
            cur_item.cur_highest_bid = bid
            cur_item.cur_highest_bidder = User.objects.get(username=request.user.username)
            credits.credit = int(credits.credit) - int(bid)
            credits.save()
            c1.credit = int(c1.credit) + int(bid)
            c1.save()
            cur_item.save()
            bt = Bought()
            bt.seller = cur_item.seller
            bt.item_id = cur_item.item_id
            bt.item_logo = cur_item.item_logo
            bt.item_name = cur_item.item_name
            bt.item_desc = cur_item.item_desc
            bt.buyer = cur_item.cur_highest_bidder
            bt.cur_highest_bid = cur_item.cur_highest_bid
            bt.created_on = cur_item.created_on
            bt.expiration = cur_item.expiration
            bt.min_price = cur_item.min_price
            bt.buy_now_price = cur_item.buy_now_price
            bt.save()
            cur_item.delete()
            messages.error(request, 'Congrats, you won!.')
            #messages.error(request, 'Congrats, you won!.')
            #cur_item = Items.objects.all()
            #cur_item = Items.objects.get(pk=item_id)
            context = {
                 'all_items': all_items,
            }

            return render(request, 'Browse/index.html', context)
        elif int(cur_item.cur_highest_bid) > int(bid) or int(cur_item.min_price) > int(bid):

            messages.error(request, 'Bid rejected.')
            cur_item = Items.objects.get(pk=item_id)
            context = {
                'cur_item': cur_item
            }
            return render(request, 'Browse/details.html', context)

    elif int(score) < int(bid):
        messages.error(request, 'You do not have enough credits!')
        cur_item = Items.objects.get(pk=item_id)
        context = {
            'cur_item': cur_item
        }
        return render(request, 'Browse/details.html', context)


def results(request):
    query = request.GET.get('search')
    item_list = Items.objects.filter(item_name__icontains=query)
    print(item_list)
    return render(request, 'Browse/index.html', {'all_items':item_list})