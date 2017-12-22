from django.conf.urls import url, include
from . import views

app_name = 'homepage'
urlpatterns = [

     url(r'^$', views.index, name='index'),
     url(r'^blog$', views.blog, name='blog'),
     url(r'^single$', views.single, name='single'),
     #url(r'^about$', views.about, name='about'),
     #url(r'^register$', include('register.urls')),
     #url(r'^register$', views.register, name='register'),
     #url(r'^login$', include('login.urls')),
]
