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

    url(r'^tutorials/$', NamedView('tutorials'), name='tutorials'),
    url(r'^tutorials/(?P<tutorial_id>\d+)/$', NamedView('tutorials'), name='tutorial_by_id'),

    url(r'^resources/$', NamedView('resources'), name='resources'),

    # these are pages used for testing things
    url(r'^components/$', NamedView('components'), name='components'),

    # a guide to text editors
    url(r'^editors/$', NamedView('editors'), name='editors'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^allforms/$', NamedView('allforms'), name='allforms'),
)

urlpatterns += patterns('',
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page': '/' }, name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)
