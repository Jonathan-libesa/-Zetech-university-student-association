"""
Django settings for Site project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import sys
import django_heroku
import dj_database_url
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

CONTENT_TYPES = ['image', 'video']
MAX_UPLOAD_SIZE = "10485760"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!je7e(18oi18$=d@+kkc!tk#w-!7-j8!4zec$e2q-f3s481(yk"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =True

ALLOWED_HOSTS = ['127.0.0.1','zetechstudentassociation.herokuapp.com']

#ALLOWED_HOSTS = ['127.0.0.1','zetechstudentassociation.herokuapp.com']

AUTH_USER_MODEL='Users.User'
# Application definition

INSTALLED_APPS = [
    'Zusa_admin',
    'About',
    'Leaders',
    'News',
    'hitcount',
    'Post',
    'ckeditor',
    'Club',
    'Main',
    'Student',
    'Alumni',
    'Users',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'storages',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'Site.urls'

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
        },
    },
]

WSGI_APPLICATION = 'Site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.postgresql',
        #'NAME':'zusa_1' ,
        #'USER':'jonathan',
        #'PASSWORD':'kenya2016',
        #'HOST':'database-1.czyinufhmlcb.us-east-2.rds.amazonaws.com',
        #'PORT':'5432'
    #}
#}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
#https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATIC_URL = '/MEDIA/'
MEDIA_URL='/Main/'
STATICFILES_DIRS =[
 os.path.join(BASE_DIR,'static')
]
MEDIA_ROOT = os.path.join(BASE_DIR,'MEDIA/Main')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_TEMPLATE_PACK="bootstrap4"




# EMAIL CONFIG
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FROM_USER = 'EMAIL_FROM_USER'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER ='jonathanlibesa@gmail.com'
EMAIL_HOST_PASSWORD = 'ibsodmfcinbftayp'
EMAIL_USE_TLS = True
EMAIL_PORT = 587


#S3 BUCKETS CONFIG

AWS_ACCESS_KEY_ID = 'AKIARPPJDDSVU7FM4NZI'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'zusa'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME = "us-east-2" # your region
AWS_S3_SIGNATURE_VERSION = "s3v4"


django_heroku.settings(locals())
