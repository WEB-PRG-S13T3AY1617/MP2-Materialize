from django.conf.urls import url, include
from . import views

app_name = 'marketplace'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.userdetails, name='userdetails'),
]
