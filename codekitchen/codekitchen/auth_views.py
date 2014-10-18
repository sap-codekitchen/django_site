from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.sites.models import get_current_site

from .auth_forms import AuthForm

def login(request, *args, **kwargs):

    redirect_to = reverse('home')

    if request.method == 'POST':
        form = AuthForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return HttpResponseRedirect(redirect_to)
        else:
            print "form wasn't valid!"
            print form.non_field_errors()
            print form.cleaned_data
    else:
        form = AuthenticationForm(request)

    current_site = get_current_site(request)
    context = {}
    if 'extra_context' in kwargs:
        context.update(kwargs.pop('extra_context'))

    context.update({
        'form': form,
        'next': redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    })

    return  TemplateResponse(request,
            'registration/login.html', context
            )



