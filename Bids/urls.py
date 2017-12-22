from django.conf.urls import url
from . import views

app_name = 'Bids'
urlpatterns = [

    url(r'^showlistings$', views.show_listings, name='showlist'),
    url(r'^showbids$', views.show_bids, name='showbid'),
    url(r'^showbought$', views.show_bought, name='showbought'),
    url(r'^(?P<item_id>[0-9]+)/$', views.details, name='detail'),
]
