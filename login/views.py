# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponseRedirect

from login import forms
from .forms import LoginForm
from Browse.models import Items
from django.contrib.auth import logout
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import View

template_name = 'login/user_form.html'


def login_view(request):
    form = LoginForm(request.POST or None)
    print(form)
    next_var = request.GET.get('next')
    print(next_var)
    print(form.is_valid())
    if form.is_valid():
        username = form.cleaned_data.get("username")
        print(username)
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next_var:
            return redirect(next_var)
        return redirect("Browse:show")

    context = {
        "form": form,
        "title": "Login",
    }
    return render(request, template_name, context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("homepage:index")
    else:
        return redirect('homepage:index')


