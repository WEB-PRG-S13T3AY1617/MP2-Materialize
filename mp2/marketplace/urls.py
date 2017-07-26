from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'marketplace'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.userdetails, name='userdetails'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', login, {'template_name': 'marketplace/login.html'}),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
