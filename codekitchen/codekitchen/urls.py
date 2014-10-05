from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from .viewclasses import NamedView
from .auth_views import login

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
    url(r'^$', NamedView('home'), name='home'),
    url(r'^blog/$', NamedView('blog'), name='blog'),
    url(r'^events/$', NamedView('events'), name='events'),
    url(r'^events/(?P<event_id>\d+)/$', NamedView('events'), name='event_by_id'),

    url(r'^resources/$', NamedView('resources'), name='resources'),
    url(r'^tutorials/$', NamedView('tutorials'), name='tutorials'),

    # these are pages used for testing things
    url(r'^components/$', NamedView('components'), name='components'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^login/$', login, name="login",),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        name="logout"),
    url(r'^password_reset/$',
        'django.contrib.auth.views.password_reset',
        name="password_reset"),
    url(r'^password_change/$',
        'django.contrib.auth.views.password_change'
        ),
    url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done'),
)
