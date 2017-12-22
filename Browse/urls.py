from django.conf.urls import url
from . import views

app_name = 'Browse'
urlpatterns = [

    url(r'^show$', views.show, name='show'),
    url(r'^(?P<item_id>[0-9]+)/$', views.details, name='detail'),
    url(r'^(?P<item_id>[0-9]+)/updated$', views.update, name='update'),
    url(r'results$', views.results, name='results'),
]
