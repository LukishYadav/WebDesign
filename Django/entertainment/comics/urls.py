from django.conf.urls import url,include
from django.contrib import admin
from comics import views
from django.conf import settings
from django.conf.urls.static import static

app_name='comics'

urlpatterns = [
      url(r'^$', views.index.as_view(),name='index'),
      url(r'^add/$', views.addcomics.as_view(),name='addcomics'),
      #url(r'^(?P<pk>[0-9]+)/$', views.detail.as_view(),name='detail'),
      url(r'^(?P<pk>[0-9]+)/$',views.detail.as_view(), name='detail'),
      url(r'^delete/(?P<pk>[0-9]+)/$', views.deletecomics.as_view(),name='delete'),

]



#SHOULD BE DONE IN MAIN SITE

"""
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

"""	