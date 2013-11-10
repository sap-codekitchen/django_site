from django.db import models

class Topic(models.Model):
    name = models.CharField( max_length=100 )
    description = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return self.name

class Member(models.Model):
    name = models.CharField( max_length=100 )
    program = models.CharField( max_length=150, null=True, blank=True )
    athena_name = models.CharField( max_length=50, null=True, blank=True )
    email = models.EmailField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    skills = models.ManyToManyField("Topic", null=True, blank=True,
            related_name="helpers")
    interests = models.ManyToManyField("Topic", null=True, blank=True,
            related_name="learners")
    homepage = models.URLField(null=True, blank=True)
    def __unicode__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField( max_length=150)
    link = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    topics = models.ManyToManyField("Topic", null=True, blank=True)
    file = models.FileField(null=True, blank=True,
            upload_to="resources")
    def __unicode__(self):
        return self.name

class Session(models.Model):
    date = models.DateField()
    attendees = models.ManyToManyField(Member, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    def __unicode__(self):
        fmt = "%a, %b %d %Y"
        return self.date.strftime(fmt)

class NewsItem(models.Model):
    title = models.CharField( max_length=100, null=True, blank=True)
    subtitle = models.CharField( max_length=150, null=True, blank=True)
    body = models.TextField()
    date = models.DateField()
    resources = models.ManyToManyField("Resource", null=True, blank=True)
    author = models.ManyToManyField("Member")
    def __unicode__(self):
        return self.title



