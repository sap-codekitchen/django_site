from kitchen.models import *
from rest_framework import serializers

"""
Serializer notes:
    `restore_object` is called to reinstantiate objects from their
    representative dictionaries.
"""

class MemberSerializer(serializers.ModelSerializer):
    interests = serializers.PrimaryKeyRelatedField(many=True)
    skills = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = Member
        fields = (
            'id',
            'name',
            'athena_name',
            'email',
            'bio',
            'skills',
            'interests',
            'homepage',
                )

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = (
                'id',
                'name',
                'description',
                )

class ResourceSerializer(serializers.ModelSerializer):
    topics = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = Resource
        fields = (
                'id',
                'name',
                'link',
                'description',
                'date_added',
                'topics',
                'file',
                )


class SessionSerializer(serializers.ModelSerializer):
    attendees = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = Session
        fields = (
                'id',
                'date',
                'attendees',
                'notes',
                )

class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = (
                'id',
                'title',
                'subtitle',
                'body',
                'date',
                'resources',
                'author',
                )



