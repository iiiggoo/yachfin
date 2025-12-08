"""
Production-ready Django settings for Yachfin project on Render.
"""

from pathlib import Path
import os
from decouple import config  # for reading .env
import dj_database_url      # for parsing DATABASE_URL

# -------------------------
#   BASE DIRECTORY
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
#   SECURITY
# -------------------------
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')


# -------------------------
#   APPLICATIONS
# -------------------------
INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
]

# -------------------------
#   MIDDLEWARE
# -------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # serve static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------
#   URL CONFIGURATION
# -------------------------
ROOT_URLCONF = 'Yachfin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Yachfin.wsgi.application'

# -------------------------
#   DATABASE
# -------------------------
db_url = config('DATABASE_URL')  # no default; must be set in .env
DATABASES = {
    'default': dj_database_url.parse(db_url, conn_max_age=600)
    }
# -------------------------
#   PASSWORD VALIDATION
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# -------------------------
#   INTERNATIONALIZATION
# -------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------
#   STATIC FILES
# -------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Yachfin/static'),
    ]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -------------------------
#   DEFAULT AUTO FIELD
# -------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
