# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import ItemUploadForm
from Browse.models import Items
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.utils.timezone import localtime, now


# Create your views here.
User = get_user_model()
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


# def what(request):
#     return render(request, 'Bids:showlist')


class ItemUploadFormView(View):
    active = 'upload'
    form_class = ItemUploadForm
    template_name = 'Sell/register_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            item = Items()
            item.item_name = form.cleaned_data['item_name']
            item.item_desc = form.cleaned_data['item_desc']
            item.min_price = form.cleaned_data['min_price']
            item.buy_now_price = form.cleaned_data['buy_now_price']
            item.expiration = form.cleaned_data['expiration']
            item.seller = User.objects.get(username=request.user.username)
            item.created_on = localtime(now())

            item.item_logo = request.FILES['item_logo']
            file_type = item.item_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {

                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, self.template_name, context)

            item.save()
            return redirect('Bids:showlist')
        return render(request, self.template_name, {'form': form}, {'active':active})


