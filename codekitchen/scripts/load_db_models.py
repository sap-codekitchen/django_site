from .add_users import add_super, add_staff
from django.utils.text import slugify
from faker import Factory

from kitchen.models import Topic

fake = Factory.create()

def create_topics():
    from .topics import initial_topics
    new_topics = []
    for name in initial_topics:
        slug = slugify(name)
        topic = Topic(name=name, slug=slug)
        topic.save()
        new_topics.append(topic)
    return new_topics

def create_supers(n=3):
    super_emails = [fake.email() for i in range(n)]
    supers = map(add_super, super_emails)
    return supers

def create_users(n=10):
    emails = [fake.email() for i in range(n)]
    users = map(add_staff, emails)
    return users

def run():
    supers = create_supers()
    users = create_supers()
    topics = create_topics()
    print supers[0].email
