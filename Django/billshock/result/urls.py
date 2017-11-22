from django.conf.urls import url
#from django.contrib import admin
from . import views

app_name='result'

urlpatterns = [
    #url(r'^$', views.hello,name='hello'),
    url(r'^$', views.listview.as_view(),name='hello'),
    url(r'^(?P<pk>[0-9]+)/$',views.detailview.as_view(),name='detail'),
    #url(r'^try/$',views.detailview.as_view(),name='detail2')
    ]
