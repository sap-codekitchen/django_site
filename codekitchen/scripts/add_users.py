from django.contrib.auth.models import User

def add_super(email):
    User.objects.create_superuser(
            username=email, email=email, password=email,
            )

def add_staff(email):
    User.objects.create_user(
            username=email, email=email, password=email,
            )

def run():
    add_super('bgolder@mit.edu')
