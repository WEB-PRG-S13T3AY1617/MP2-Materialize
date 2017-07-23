from django.conf.urls import url, include
from . import views

app_name = 'marketplace'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^userdetails/(?P<user_id>[0-9]+)/$', views.userdetails, name='userdetails'),
    url(r'^registration/$', views.registration, name='registration'),
]
