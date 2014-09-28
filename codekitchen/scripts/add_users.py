from django.contrib.auth.models import User

def run():
    user = User.objects.create_user(
            'bgolder', 'bgolder@mit.edu', 'bgolder'
            )
