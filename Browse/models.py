# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import localtime, now


class Items(models.Model):
    seller = models.ForeignKey(User, null=True)
    item_id = models.AutoField(primary_key=True)
    item_logo = models.FileField(null=True, blank=True)
    item_name = models.CharField(max_length=2500)
    item_desc = models.TextField(max_length=2500)
    cur_highest_bidder = models.ForeignKey(User, related_name="highest_bidder", null=True, blank=True)
    cur_highest_bid = models.IntegerField(null=True, default=0)
    created_on = models.DateTimeField(null=True)
    expiration = models.DateTimeField(null=True)
    min_price = models.IntegerField(null=True)
    buy_now_price = models.IntegerField(null=True)

    def __str__(self):
        return self.item_name
# Create your models here.


class Bought(models.Model):
    seller = models.ForeignKey(User, null=True)
    item_id = models.AutoField(primary_key=True)
    item_logo = models.FileField(null=True, blank=True)
    item_name = models.CharField(max_length=2500)
    item_desc = models.TextField(max_length=2500)
    buyer = models.ForeignKey(User, related_name="buyer", null=True, blank=True)
    cur_highest_bid = models.IntegerField(null=True, default=0)
    created_on = models.DateTimeField(null=True)
    expiration = models.DateTimeField(null=True)
    min_price = models.IntegerField(null=True)
    buy_now_price = models.IntegerField(null=True)
    #sell_price = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.item_name


class Expired(models.Model):
    seller = models.ForeignKey(User, null=True)
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=2500)
    item_desc = models.TextField(max_length=2500)
    created_on = models.DateTimeField(default=localtime(now()))
    min_price = models.IntegerField(null=True)
    buy_now_price = models.IntegerField(null=True)

    def __str__(self):
        return self.item_name
