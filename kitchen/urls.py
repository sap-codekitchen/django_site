from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'kitchen.views.index', name='index'),
    #url(r'^members/$', 'kitchen.views.members', name='members'),
    #url(r'^resources/$', 'kitchen.views.resources', name='resources'),

)
