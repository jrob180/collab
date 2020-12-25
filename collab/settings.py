"""
Django settings for collab project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!2k-i*!=q^o^*uapjn68mu3#l9t9b97tt88bf4-vv-(bl3hp-u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#test
ALLOWED_HOSTS = [
    '737899e9175e.ngrok.io',
    '127.0.0.1',
    'localhost',
    'ee562bb8e2d1.ngrok.io',
    '554516b85f73.ngrok.io',
    '689f071b91a6.ngrok.io',
    'ba4f4b1cfa1e.ngrok.io',
    'aa2bd4fff57f.ngrok.io',
    'dd5fb990096c.ngrok.io',
    'bb24e4822392.ngrok.io',
    'collabrooms-prod-env.eba-yd7yre6h.us-west-2.elasticbeanstalk.com',
    '172.31.40.199',
    'collabrooms.io',
    'www.collabrooms.io',
    '67be1a47ffc6.ngrok.io',
    'collabrooms-school-env.eba-3gdpj2qu.us-west-2.elasticbeanstalk.com',
    '7cf650b2b52e.ngrok.io',
    '1e3c037450c8.ngrok.io',
    '0925480b6346.ngrok.io',
]


# Application definition

INSTALLED_APPS = [
    'studyApp.apps.StudyappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth', 
    'allauth.account', 
    #'social_auth', 
    'allauth.socialaccount',   
    'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.adapter',
    #'background_task',
    #'django_crontab',
    #'django_pg',  
    'ckeditor',
    'ckeditor_uploader',
]

CKEDITOR_UPLOAD_PATH = 'uploads/'

SOCIALACCOUNT_ADAPTER = 'studyApp.adapters.MySocialAccount'

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'collab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        'libraries':{
            'joinroom': 'studyApp.templatetags.joinroom',

            }
        },
    },
]


WSGI_APPLICATION = 'collab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': os.path.join(BASE_DIR, 'postgreSQL'),

        'USER': 'arulkapoor118',

        'PASSWORD': 'q123q123',

        'HOST': '689f071b91a6.ngrok.io',

        'PORT': '8000',


    }
}'''


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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    #'social_auth.backends.google.GoogleOAuth2Backend',

)

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/login'
ACCOUNT_LOGOUT_ON_GET = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
SOCIAL_AUTH_PIPELINE =  (

    'social_core.pipeline.social_auth.auth_allowed',
)
# SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {
#     'hd': 'columbia.edu',
#     'access_type': 'online',
# }


STATIC_URL = '/static/'
STATIC_ROOT = 'static'


#CRONJOBS = [
#    ('*/1 * * * *', 'studyApp.cron.refresh_access_token')
#]

CKEDITOR_CONFIGS = {
    'default':
        {'toolbar': 'Custom', 
         'toolbar_Custom': [
            ['Bold', 'Link', 'Unlink', 'Image'], 
        ], 
}}

DJRICHTEXTFIELD_CONFIG = {
    'js': ['//cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link image',
        'toolbar': 'bold italic | link image | removeformat',
        'width': 700
    }
}