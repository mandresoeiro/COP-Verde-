import sys
import os
from pathlib import Path

# 📁 Caminho base do projeto (ex: /backend)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 🧠 Adiciona a pasta 'apps/' ao PYTHONPATH para permitir imports como from accounts.models import ...
sys.path.append(str(BASE_DIR / "apps"))

# ⚠️ SECRET_KEY apenas para desenvolvimento — use .env com python-decouple em produção
SECRET_KEY = 'django-insecure-eaw-j&c&_=mal$3^=bhqvq3z%qk_($=jgr1%e=ghk5(icvxqnf'

# ⚙️ Debug e hosts devem ser definidos em dev.py ou prod.py
DEBUG = False
ALLOWED_HOSTS = []

# 🌍 Configuração do site para allauth (obrigatório)
SITE_ID = 1

# 🧩 Aplicativos nativos do Django
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

# 🔌 Apps de terceiros
THIRD_PARTY_APPS = [
    'corsheaders',  # ← ADICIONADO
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'dj_rest_auth.registration',
]

# 🧱 Apps do seu projeto
PROJECT_APPS = [
    'apps.accounts',
    'apps.places',
]

# ✅ Todos os apps juntos
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

# 🧱 Middlewares
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # ← OBRIGATORIAMENTE ANTES do CommonMiddleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌐 Rotas principais
ROOT_URLCONF = 'core.urls'

# 🖼️ Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🚪 WSGI
WSGI_APPLICATION = 'core.wsgi.application'

# 🛢️ Banco de dados virá em dev.py/prod.py
DATABASES = {}

# 🌎 Localização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Belem'
USE_I18N = True
USE_TZ = True

# 📦 Arquivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# 📁 Arquivos de mídia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🔑 Chave primária padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔐 Autenticação
AUTH_USER_MODEL = 'accounts.User'

# 🔐 Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}

# 🌐 CORS (para funcionar com o frontend React/Vite)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # porta padrão do Vite
]
