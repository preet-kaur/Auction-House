from django import views
from django.conf.urls import url

from .views import (login_view,
                    #logout_view,
                    #register_view,
                    # auth_view
                    )

app_name = 'login'
urlpatterns = [

     #url(r'^what$', views.what, name='what'),
     url(r'^$', views.login_view, name='login'),
     url(r'^logout/$', views.logout_view, name='logout')
]
