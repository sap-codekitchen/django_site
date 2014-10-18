from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.conf import settings

class TemplateView():
    def __init__(self, template, context=None ):
        self.template = template
        if not context:
            context = {}
        self.context = context

    def __call__(self, request):
        return render( request, self.template, self.context)

class NamedView():
    def __init__(self, name, context=None):
        if not context:
            context = {}
        self.context = {}
        self.name = name
        self.template = name + ".html"
        # set defaults
        self.context['pagetitle'] = name.capitalize() + ' - CodeKitchen - MIT'
        self.context['pageclass'] = name
        self.context.update(context)
        self.context['AUTH_ROOT_URL'] = settings.AUTH_ROOT_URL

    def __call__(self, request, *args, **kwargs):
        self.add_navlinks()
        return render( request, self.template, self.context)

    def add_navlinks(self):
        navlinks = []
        for nav in ('blog', 'resources', 'events'):
            navlink = {
                    'text': nav,
                    'url': reverse(nav)
                    }
            if nav == self.name:
                self.context['linktrail'] = [navlink]
            navlinks.append(navlink)
        self.context['navlinks'] = navlinks







