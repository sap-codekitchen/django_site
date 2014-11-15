from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth import login

from django.contrib.auth.forms import AuthenticationForm

class NamedView():
    def __init__(self, name, context=None):
        self.context = {}
        self.custom_context = context
        self.name = name
        self.template = name + ".html"

    def __call__(self, request, *args, **kwargs):
        self.add_base_context()
        self.add_navlinks()
        self.add_custom_context()
        return render( request, self.template, self.context)

    def add_custom_context(self):
        if self.custom_context:
            self.context.update(self.custom_context)

    def add_base_context(self):
        self.context['pagetitle'] = self.name.capitalize() + ' - CodeKitchen - MIT'
        self.context['pageclass'] = self.name
        self.context['AUTH_ROOT_URL'] = settings.AUTH_ROOT_URL
        self.context['ROOT_URL'] = settings.ROOT_URL

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


class LoginView(NamedView):
    def __init__(self, context=None):
        NamedView.__init__(self, 'login', context)
        self.template = "registration/login.html"

    def __call__(self, request, *args, **kwargs):
        self.context = {}
        if request.POST:
            form = AuthenticationForm(request, data=request.POST)
            nextpage = request.POST.get('next', settings.ROOT_URL)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect(nextpage)
            else:
                errors = form.errors['__all__']
                self.context.update({'form': form,
                    'next': nextpage, 'errors': errors})
        else:
            self.context['next'] = request.GET.get('next', settings.ROOT_URL)
        self.add_base_context()
        self.add_navlinks()
        self.add_custom_context()
        return render( request, self.template, self.context)



