# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class register(models.Model):
     user_id = models.AutoField(primary_key=True)
    #user_name = models.CharField(max_length=500, null=True)
   # user_email = models.CharField(max_length=500,  null=True)
   # user_mobile = models.IntegerField( null=True)
   # user_password = models.CharField(max_length=500,  null=True)
     user_dob = models.DateField(("date of birth"),  null=True)
     user_credits = models.IntegerField(default=1000,  null=True)

def get_absolute_url(self):
        return 'register:register'

def __str__(self):
        return self.user_name

# Create your models here.
