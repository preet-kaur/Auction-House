from django.conf.urls import url
from . import views

app_name = 'register'
urlpatterns = [
    #url(r'^what$', views.what, name='what'),
    #url(r'^registration$', views.registration, name='what'),
    url(r'^$', views.UserFormView.as_view(), name='register'),
]
