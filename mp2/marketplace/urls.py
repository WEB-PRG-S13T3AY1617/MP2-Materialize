from django.conf.urls import url
from django.contrib.auth.views import logout
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'marketplace'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.userdetails, name='userdetails'),
    url(r'^photo/(?P<post_id>[0-9]+)/$', views.photo, name='photo'),
    url(r'^offer/(?P<post_id>[0-9]+)/$', views.makeoffer, name='makeoffer'),
    url(r'^update/(?P<myoffer_id>[0-9]+)/$', views.updateoffer, name='updateoffer'),
    url(r'^approve/(?P<offer_id>[0-9]+)/$', views.approveoffer, name='approveoffer'),
    url(r'^reject/(?P<offer_id>[0-9]+)/$', views.rejectoffer, name='rejectoffer'),
    url(r'^delete/(?P<myoffer_id>[0-9]+)/$', views.canceloffer, name='canceloffer'),
    url(r'^results/condition/(?P<condition_name>[-\w ]+)/$', views.condresults, name='condresults'),
    url(r'^results/type/(?P<type_name>\w+)/$', views.typeresults, name='typeresults'),
    url(r'^results/course/(?P<course_name>[-\w ]+)/$', views.courseresults, name='courseresults'),
    url(r'^results/tags/(?P<tag_name>[-\w]+)/$', views.tagresults, name='tagresults'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
