from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.conf import settings

class NamedView():
    def __init__(self, name, context=None):
        self.context = {}
        self.name = name
        self.template = name + ".html"
        # set defaults
        self.context['pagetitle'] = name.capitalize() + ' - CodeKitchen - MIT'
        self.context['pageclass'] = name
        self.context['AUTH_ROOT_URL'] = settings.AUTH_ROOT_URL
        self.context['ROOT_URL'] = settings.ROOT_URL
        if context:
            self.context.update(context)

    def __call__(self, request, *args, **kwargs):
        self.add_navlinks()
        return render( request, self.template, self.context)

    def add_navlinks(self):
        navlinks = []
        for nav in ('blog', 'resources', 'events'):
            navlink = {
                    'text': nav,
                    'url': settings.ROOT_URL + reverse(nav)
                    }
            if nav == self.name:
                self.context['linktrail'] = [navlink]
            navlinks.append(navlink)
        self.context['navlinks'] = navlinks







