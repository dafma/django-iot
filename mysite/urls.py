from django.conf.urls import patterns, include, url

from iot.api import iot_router

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^iot/', include('iot.urls', namespace="iot")),
    url(r'^admin/', include(admin.site.urls)),
    #todo: this should probably be included inside iot url registration instead  (look into where it should belong)
    url(r'^api/', include(iot_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
)