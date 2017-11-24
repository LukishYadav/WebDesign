from django.conf.urls import include, url
from . import views


app_name='music'
urlpatterns = [
    #/music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/music/71/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),

    #/music/album/add
    url(r'^album/add/$',views.AlbumCreate.as_view(),name='album-add'), 

    #/music/album/2
    url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),


    url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),
    #/music/71/
    #url(r'^(?P<album_id>[0-9]+)/favorite $',views.favorite, name='favorite'),
]