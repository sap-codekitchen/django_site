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

from kitchen.serializers import *

from codekitchen.settings import TEMPLATE_DIRS



def filterByIds(ids, objs, idfield="id"):
    for obj in objs:
        if obj[idfield] in ids:
            yield obj

def linkObject(thing, linkfield, otherset):
    thing[linkfield] = filterByIds(
            thing[linkfield],
            otherset)

def all_objects():
    context = {
        'topics': TopicSerializer(
            Topic.objects.all(), many=True).data,
        'members': MemberSerializer(
            Member.objects.all(), many=True).data,
        'resources': ResourceSerializer(
            Resource.objects.all(), many=True).data,
        'sessions': SessionSerializer(
            Session.objects.all(), many=True).data,
        'newsitems': NewsItemSerializer(
            NewsItem.objects.all(), many=True).data,
    }
    for member in context['members']:
        linkObject(member, 'interests', context['topics'])
        linkObject(member, 'skills', context['topics'])
    for session in context['sessions']:
        linkObject(session, 'attendees', context['members'])
    return context

def all_resources():
    context = {
        'resources': ResourceSerializer(
            Resource.objects.all(), many=True).data,
        'topics': TopicSerializer(
            Topic.objects.all(), many=True).data,
            }
    for resource in context['resources']:
        linkObject(resource, 'topics', context['topics'])
    return context

def index(request):
    context = {
            "page_title": "CodeKitchen | MIT SA+P",
            }
    context.update(all_objects())
    return render_to_response(
            'index.html',
            RequestContext(request, context),
            )

def resources(request):
    context = {
            "page_title": "Resources | CodeKitchen | MIT SA+P",
            }
    context.update( all_resources() )
    return render_to_response(
            'resources.html',
            RequestContext(request, context),
            )

