from django.conf.urls import url
#from django.contrib import admin
from . import views

app_name='result'

urlpatterns = [
    #url(r'^$', views.hello,name='hello'),
    url(r'^$', views.listview.as_view(),name='hello'),
    url(r'^(?P<pk>[0-9]+)/$',views.detailview.as_view(),name='detail'),

    url(r'^data/add/$',views.add.as_view(),name='add'),
    url(r'^data/delete/(?P<pk>[0-9]+)$',views.delete.as_view(),name='delete'),
    #url(r'^try/$',views.detailview.as_view(),name='detail2')
    ]
