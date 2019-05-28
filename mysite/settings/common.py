"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd#6xh^9&f_6e=*k=!8(&nkje@i8dc=divjz=*ljx$n&v1qb001'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]


# Application definition
INSTALLED_APPS = [
    'staff',
    'quiz',
    'plant',
    'user',
    'django_summernote',  # 추가 ---------------------------------------------------------------
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',
    # 'django.contrib.humanize',
    
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mysite', 'templates')],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
            'ENGINE':   'django.db.backends.mysql',
            'NAME':     'threewheel',                  # DB 이름
            'USER':     'root',                    # DB 사용자 이름
            'PASSWORD': 'mysql1111',              # DB 비밀번호
            'HOST':     '127.0.0.1',               # DB 서버 주소
            'PORT':     '',                        # DB 포트 (생략하면 MySQL 디폴트 포트 3306 자동 지정)
            'OPTIONS':  {'charset': 'utf8mb4'},
        }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'threequizreal$threewheel',                  # DB 이름
#         # 'TEST': {
#         #             'NAME': 'homework$test_threewheel',
#         #         },
#         'USER':     'threequizreal',                    # DB 사용자 이름
#         'PASSWORD': 'mysql1111',              # DB 비밀번호
#         'HOST':     'threequizreal.mysql.pythonanywhere-services.com',               # DB 서버 주소
#         'PORT':     '',                        # DB 포트 (생략하면 MySQL 디폴트 포트 3306 자동 지정)
#         'OPTIONS':  {
#             'charset': 'utf8mb4',
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#         },
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'mysite', 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'  # 항상 '/'로 끝나야 함
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
INTERNAL_IPS = ['127.0.0.1']                            # 추가 3
LOGIN_REDIRECT_URL = '/'
SITE_ID = 1

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sindpfla@gmail.com'
EMAIL_HOST_PASSWORD = 'bufgsdvwlekcklbn'
EMAIL_USE_TLS = True

AUTH_USER_MODEL = 'user.User'


# 5.28 소이 - summernote 설정
SUMMERNOTE_CONFIG = {
    'attachment_filesize_limit': 1024*1024*10, # specify the file size
}