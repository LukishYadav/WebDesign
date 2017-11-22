from django.conf.urls import url
#from django.contrib import admin
from . import views

app_name='result'

urlpatterns = [
    url(r'^$', views.hello,name='hello'),
    ]
