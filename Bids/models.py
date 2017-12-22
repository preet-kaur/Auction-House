# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Credits(models.Model):
    name = models.ForeignKey(User, unique=True)
    credit = models.IntegerField(null=True, default=10000)

    #def __str__(self):
     #   return self.name.first_name