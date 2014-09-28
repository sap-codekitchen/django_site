from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render

class TemplateView():
    def __init__(self, template, context=None ):
        self.template = template
        self.context = context

    def __call__(self, request):
        return render( request, self.template, self.context)


