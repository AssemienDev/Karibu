"""
Django settings for espaceKaribu project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

import mimetypes
import pymysql


mimetypes.add_type("text/javascript", ".js", True)

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r@ia+bhsr46uicv37agw)3bmhx*@+kl2+i94lscjoe6cg1o1y2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['espacekaribu.com', 'www.espacekaribu.com']

BASE_URL = 'https://espacekaribu.com'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pwa',
    'utilisateur.apps.UtilisateurConfig',
    'django.contrib.sitemaps',
    'administrateur.apps.AdministrateurConfig'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'espaceKaribu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [BASE_DIR / 'templates']
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  
            os.path.join(BASE_DIR, 'templates', 'admin'),  
            os.path.join(BASE_DIR, 'templates', 'utilisateur'), 
        ]
        ,
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

WSGI_APPLICATION = 'espaceKaribu.wsgi.application'


#Les fichiers static
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


#Pour le deploiement
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#Pour les session
SESSION_ENGINE = 'django.contrib.sessions.backends.db'


#Sauvegarde des media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

#pour ousbi
"""DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'espace_karibu_bd',
      'USER': 'root',
      'PASSWORD': '',
      'HOST': 'localhost',
      'PORT': '3306',
  }
}

# BD DE MARIE
DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'espace_karibu_bd',
           'USER': 'root',
           'PASSWORD': 'root',
           'HOST': 'localhost',
           'PORT': '3307',
       }
 }"""


DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'c2587844c_espace_karibu_bd',
      'USER': 'c2587844c_espace',
      'PASSWORD': 'Assemien12@',
      'HOST': 'localhost',
      'PORT': '3306',
      'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
  }
}


# Temps de vie d'une session
SESSION_COOKIE_AGE = 60 * 60 * 3
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
#Les fichiers static
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

#Pour le deploiement
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#Envoi d'email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'espacekaribu1308@gmail.com'
EMAIL_HOST_PASSWORD = 'afkvxicvyvntopfd '
DEFAULT_FROM_EMAIL = 'espacekaribu1308@gmail.com'




PWA_APP_NAME = 'Espace karibu'
PWA_APP_DESCRIPTION = "My app description"
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/karibu/assets/images/logo1.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/karibu/assets/images/logo1.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/karibu/assets/images/logo1.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
PWA_APP_SHORTCUTS = [
    {
        'name': 'Shortcut',
        'url': '/target',
        'description': 'Shortcut to a page in my application'
    }
]
PWA_APP_SCREENSHOTS = [
    {
      'src': '/static/karibu/assets/images/logo1.png',
      'sizes': '750x1334',
      "type": "image/png"
    }
]

