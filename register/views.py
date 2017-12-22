# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import register
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import View

from Bids.models import Credits
from register.models import register
from .forms import UserForm
from django.http import HttpResponseRedirect

User = get_user_model()


# Create your views here.
class register_user(CreateView):
    # model = register
    fields = ['user_name', 'user_email', 'user_mobile', 'user_password', 'user_dob']


def registration(request):
    return render(request, 'register/register_form.html')


def registers(request):
    if request.method == 'POST':
        r = register()
        name = request.POST['user_name']
        email = request.POST['user_email']
        mobile = request.POST['user_mobile']
        password = request.POST['user_password']
        dob = request.POST['user_dob']
        r = register(user_name=name, user_email=email, user_dob=dob, user_mobile=mobile, user_password=password)
        r.save()

        return render(request, 'register/register.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'register/register_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print(form.is_valid())
        if form.is_valid():
            cred = Credits()

            user = form.save(commit=False)
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            username = form.cleaned_data['username']
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    cred.name = User.objects.get(username=request.user.username)
                    cred.credit = 10000
                    cred.save()
                    return redirect("Browse:show")

        return render(request, self.template_name, {'form': form})
