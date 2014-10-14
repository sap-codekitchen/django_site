from .add_users import add_super, add_staff
from faker import Factory

fake = Factory.create()

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
    print supers[0].email
