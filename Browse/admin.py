# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Expired
from .models import Bought
from .models import Items

# Register your models here.
admin.site.register(Items)
admin.site.register(Bought)
admin.site.register(Expired)