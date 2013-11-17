from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'kitchen.views.index', name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

)
