from django.conf.urls import patterns, url

from iot import views

urlpatterns = patterns('',	
	url(r'^$', views.IndexView.as_view(), name='index'),	
	url(r'^(?P<pk>[^/]+)/$', views.DeviceDetailView.as_view(), name='devicedetail'),
)