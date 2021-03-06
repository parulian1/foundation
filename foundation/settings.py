"""
Django settings for foundation project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k_n)kka8cdadgq32g!fu8=f6vq#ip7e4jb!%yy&*3f7bdg-%1='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'tinymce',
    'paypal.standard.ipn',
    'django_markwhat',
    # 'blog.apps.BlogConfig',
    'news.apps.NewsConfig',
    'program.apps.ProgramConfig',
    'gallery.apps.GalleryConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'foundation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'context_processors.media_url',
                'context_processors.static_url',
                'context_processors.blog_media_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'foundation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'foundation',
        'USER': 'dev',
        'PASSWORD': 'dev',
        'HOST': 'localhost',
        'PORT': '',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

THUMBNAIL_DEBUG = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL_PATH = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = STATIC_URL_PATH

MEDIA_URL_PATH = '/media/'
MEDIA_URL = 'http://localhost' + MEDIA_URL_PATH

BLOG_MEDIA_URL_PATH = '/blog/media/'
BLOG_MEDIA_URL = 'http://localhost' + BLOG_MEDIA_URL_PATH

# STATICFILES_DIRS = [
#     "/static",
#     "/media/",
#     "/blog/media/",
#     "/program/media/",
#     "/news/media/",
# ]

# Path to gallery. Relative to MEDIA_ROOT. Ends with slash.
# Default if not specified: "file/".
GALLERY_PATH = 'file/'


import logging
from logging.handlers import MemoryHandler, TimedRotatingFileHandler

LOGS_DIR = os.path.join(BASE_DIR, 'logs')
LOG_FILENAME = os.path.join(LOGS_DIR, 'foundation.log')

LOG_FORMAT = '%(asctime)s %(levelname)8s %(module)s.%(funcName)s:%(lineno)d: %(message)s'
formatter = logging.Formatter(LOG_FORMAT)
LOG_HANDLER = TimedRotatingFileHandler(LOG_FILENAME, 'midnight', 0, 14)
LOG_HANDLER.setFormatter(formatter)

LOGGER = logging.getLogger('foundation')
#LOGGER.setLevel(logging.DEBUG if DEBUG else logging.INFO)
LOGGER.setLevel(logging.DEBUG)
if len(LOGGER.handlers) == 0:
    console = logging.StreamHandler()
    console.setLevel(logging.WARN)
    console.setFormatter(formatter)
    LOGGER.addHandler(LOG_HANDLER)
    LOGGER.addHandler(console)
##################################################################################################
MARKITUP_FILTER = ('django.contrib.markup.templatetags.markup.textile', {})
PAYPAL_RECEIVER_EMAIL = "martogi.parulian86@gmail.com"

try:
    from foundation.settings_local import *
except ImportError:
    pass