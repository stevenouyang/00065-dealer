from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = [
    "https://denza-indonesia.id",
    "denza-indonesia.id",
    "localhost",
    "127.0.0.1",
    "100.118.34.31",
]

CSRF_TRUSTED_ORIGINS = [
    "https://denza-indonesia.id",
    "denza-indonesia.id",
    "localhost",
    "127.0.0.1",
    "100.118.34.31",
]

SECRET_KEY = "django-insecure-n)i+ufgod+!f*ouq7%k(45imfs%%#z)^lk27ta8m%bnx##&qm3"

AWS_S3_ENDPOINT_URL = "http://nos.wjv-1.neo.id"


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "default_acl": "public-read",  # Ensures files are publicly accessible
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "location": "static/",
            "default_acl": "public-read",  # Set public-read ACL for static files
            "endpoint_url": "https://nos.wjv-1.neo.id",
        },
    },
}

# IMAGEKIT_DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "rafael01"),
        "USER": os.environ.get("DB_USER", "devadmin"),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "10.217.0.1"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}


STATIC_URL = "https://nos.wjv-1.neo.id/static/"

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


try:
    from .local import *
except ImportError:
    pass
