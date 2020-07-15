"""
Django settings for somikoron_ecommerce project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.urls import reverse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tn=0(p3qsx(_!9psep368ni1^j@@1i&m$^shk%9pk4l#8+vu_i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'mathfilters',
    'serializers',
    'rest_framework',
    # allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

    # my_apps
    'customer',
    'shop',
    'search',
]

SITE_ID = 2
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'somikoron_ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS'    : [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS' : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'somikoron_ecommerce.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE'  : 'django.db.backends.postgresql',
        # 'NAME'    : 'db_somikoron',
        # 'USER'    : 'postgres',
        # 'PASSWORD': '1234',
        # 'HOST'    : '127.0.0.1',
        # 'PORT'    : '5432',

        'ENGINE'  : 'django.db.backends.sqlite3',
        'NAME'    : os.path.join(BASE_DIR, 'db.sqlite3'),
        'HOST'    : '',
        'PORT'    : '',
        'USER'    : '',
        'PASSWORD': '',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = 'staticfiles'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

MEDIA_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'

LOGIN_URL = '/accounts/login'
# reverse('account_login')
LOGIN_REDIRECT_URL = "/"

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
         {'METHOD'        : 'oauth2',
          'SCOPE'         : ['email', 'public_profile', 'user_friends'],
          'AUTH_PARAMS'   : {'auth_type': 'reauthenticate'},
          'FIELDS'        : [
              'id',
              'email',
              'name',
              'first_name',
              'last_name',
              'verified',
              'locale',
              'timezone',
              'link',
              'gender',
              'updated_time'],
          'EXCHANGE_TOKEN': True,
          'LOCALE_FUNC'   : lambda request: 'kr_KR',
          'VERIFIED_EMAIL': False,
          'VERSION'       : 'v2.4'}}
# facebook
SOCIAL_AUTH_FACEBOOK_KEY = '629271397680203'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'e4a51b5b5c3e919ec82a2fdb5840a675'  # app key
ACCOUNT_LOGOUT_ON_GET = True
CRISPY_TEMPLATE_PACK = 'bootstrap4'

REST_FRAMEWORK = {
    'DEFAULT_METADATA_CLASS': None,
}
if DEBUG:
    # the default value
    REST_FRAMEWORK['DEFAULT_METADATA_CLASS']: 'rest_framework.metadata.SimpleMetadata'
