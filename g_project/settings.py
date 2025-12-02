"""
Django settings for g_project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url  # for parsing DATABASE_URL (optional)

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------
# INSTALLED APPS
# ----------------------
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'shop',
    'orders',
    'cart',
]

# ----------------------
# MIDDLEWARE
# ----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------
# ROOT URL CONFIG
# ----------------------
ROOT_URLCONF = 'g_project.urls'

# ----------------------
# TEMPLATES
# ----------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # add your template folder
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

# ----------------------
# WSGI
# ----------------------
WSGI_APPLICATION = 'g_project.wsgi.application'



ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

# ----------------------
# DATABASE CONFIGURATION
# ----------------------

    # Render PostgreSQL
DATABASES = {
        "default": {
            "ENGINE": 'django.db.backends.postgresql',
            "NAME": os.getenv("POSTGRES_DB"),
            "USER": os.getenv("POSTGRES_USER"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": os.getenv("POSTGRES_HOST"),
            "PORT": os.getenv("POSTGRES_PORT", "5432"),
        }
    }


# ----------------------
# AUTH PASSWORD VALIDATORS
# ----------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ----------------------
# LANGUAGE & TIMEZONE
# ----------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# ----------------------
# STATIC FILES
# ----------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# ----------------------
# MEDIA FILES
# ----------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ----------------------
# DEFAULT AUTO FIELD
# ----------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ----------------------
# LOGIN URL
# ----------------------
LOGIN_URL = '/accounts/login/'
