from django.conf.urls import patterns, include, url
import kitchen

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', include('kitchen.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
