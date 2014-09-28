import os
from .shared_private import BASE_DIR, REPO_DIR

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'codekitchen.urls'

WSGI_APPLICATION = 'codekitchen.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# directories that contain static files
STATICFILES_DIRS = (
        os.path.join(REPO_DIR, 'static'),
        )

# directories where templates may be found
TEMPLATE_DIRS = (
        os.path.join(REPO_DIR, 'templates'),
        os.path.join(REPO_DIR, 'static'),
            )

# destination to which static files will be copied
# before deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


