from django.conf.urls import patterns, include, url
import kitchen

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('kitchen.views',
    url(r'^$', 'index', name='index'),
    url(r'^resources/$', 'resources', name='resources'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
