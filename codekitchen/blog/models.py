from django.db import models

"""
Resources should include a few distinct kinds of information
    - links to things
    - files
    - events

We want to be able to classify resources

I should separate links and files and event times from the resource object.

In general, I would expect one link per resource, but one or more files.

People can zip up the files if they need to I suppose.

"""


class Resource(models.Model):
    pass

class ResourceType(models.Model):
    pass

class TimeBasedResource(Resource):
    pass

class Tag(models.Model):
    pass

class Post(models.Model):
    pass

class LongFormPost(models.Model):
    pass
