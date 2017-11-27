from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView



app_name='music'
urlpatterns = [
    #/music/
    url(r'^$', views.IndexView.as_view(), name='index'),



    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #/music/71/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),

    #/music/album/add
    url(r'^album/add/$',views.AlbumCreate.as_view(),name='album-add'), 

    #/music/album/2
    url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),


    url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),
    
    url(r'^song/add/(?P<pk>[0-9]+)/$',views.SongCreate.as_view(),name='song-add'),


    #url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'music/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'music/logged_out.html'}, name='logout'),
    #/music/71/
    #url(r'^(?P<album_id>[0-9]+)/favorite $',views.favorite, name='favorite'),
]