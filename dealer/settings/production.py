from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = [
    "citra8.id",
    "https://denza-indonesia.id",
    "localhost",
    "127.0.0.1",
    "100.118.34.31",
]

CSRF_TRUSTED_ORIGINS = [
    "citra8.id",
    "https://denza-indonesia.id",
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
        "NAME": "rafael01",
        "USER": "devadmin",
        "PASSWORD": "testsatuduatiga",
        "HOST": "103.150.101.6",
        "PORT": "5431",
    }
}


STATIC_URL = "https://nos.wjv-1.neo.id/static/"

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


try:
    from .local import *
except ImportError:
    pass
