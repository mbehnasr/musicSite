from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/712/ == /music/album_id/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]
