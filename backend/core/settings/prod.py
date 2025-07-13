from .base import *
import os
from decouple import config

DEBUG = False

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['seusite.com', 'www.seusite.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}
