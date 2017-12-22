from django.shortcuts import render



# Create your views here.

def login(request):
    return render(request, 'login/user_form.html')


def register(request):
    return render(request, 'register/register_form.html')


def index(request):
    active = 'home'
    return render(request, 'homepage/index.html',{'active':active})


def single(request):
    return render(request, 'homepage/single.html')


def blog(request):
    return render(request, 'homepage/blog.html')


def about(request):
    return render(request, 'homepage/index.html')
