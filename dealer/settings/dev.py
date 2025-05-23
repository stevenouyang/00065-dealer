from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-n)i+ufgod+!f*ouq7%k(45imfs%%#z)^lk27ta8m%bnx##&qm3"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "default_acl": "public-read",  # Ensures files are publicly accessible
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# IMAGEKIT_DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "rafael01",
        "USER": "devadmin",
        "PASSWORD": "testsatuduatiga",
        "HOST": "103.150.101.6",
        "PORT": "5431",
    }
}

try:
    from .local import *
except ImportError:
    pass
