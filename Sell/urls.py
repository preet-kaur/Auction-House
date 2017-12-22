from django.conf.urls import url
from . import views

app_name = 'Sell'
urlpatterns = [

    url(r'^$', views.ItemUploadFormView.as_view(), name='upload'),
    #url(r'^what$', views.what, name='what'),

]
