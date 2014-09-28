from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from .views import home

"""
Login --> see your home page
logout --> see the home page

r'^login/$'
    login form needs a password reset link
r'^logout/$'
r'^password_reset/$'
r'^password_reset_confirm/$'
r'^password_change/$'
r'^password_change_done/$'
"""

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change'),
    url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done'),
)
