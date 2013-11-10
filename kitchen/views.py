import os
import shutil
import random
import json
import datetime
import urllib
from pprint import pprint

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from kitchen.models import (
        Topic,
        Member,
        Resource,
        Session,
        NewsItem,
        )

def all_objects():
    context = {
        'topics': Topic.objects.all(),
        'members': Members.objects.all(),
        'resources': Resources.objects.all(),
        'sessions': Session.objects.all(),
        'newsitems': NewsItem.objects.all(),
            }
    return context

def index(request):
    context = {
            "page_title": "MIT SA+P homepage",
            }
    return render_to_response(
            'index.html',
            RequestContext(request, c),
            )

