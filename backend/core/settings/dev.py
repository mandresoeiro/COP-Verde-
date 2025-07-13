# core/settings/dev.py

from .base import *
from decouple import config, Csv

# ==========================
# ⚙️ Configurações Gerais
# ==========================

DEBUG = config('DEBUG', cast=bool, default=True)
DEBUG_PROPAGATE_EXCEPTIONS = True  # Exibe traceback completo no navegador (útil no desenvolvimento)

# Chave secreta vinda do .env
SECRET_KEY = config('SECRET_KEY')

# Hosts permitidos durante o desenvolvimento
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default='127.0.0.1,localhost')

# ==========================
# 🗃 Banco de Dados (SQLite para Dev)
# ==========================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==========================
# 🔗 Django REST Framework
# ==========================

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

