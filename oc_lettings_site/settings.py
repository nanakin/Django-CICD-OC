import logging
import os
from pathlib import Path

import sentry_sdk
from decouple import config, Csv
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Application definition

INSTALLED_APPS = [
    'lettings',
    'profiles',
    'oc_lettings_site.apps.OCLettingsSiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

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

ROOT_URLCONF = 'oc_lettings_site.urls'

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

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

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

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static", ]

STORAGES = {
    "staticfiles": {"BACKEND": 'whitenoise.storage.CompressedStaticFilesStorage'}
}

# Logging

logging.basicConfig(level=logging.INFO)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {message}',
                'style': '{',
            },
        },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        # 'file': {
        #     'class': 'logging.FileHandler',
        #     'filename': BASE_DIR / 'general.log',
        #     'formatter': 'verbose'
        # },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": config('DJANGO_LOG_LVL', default='INFO'),
            "propagate": False,
        },
        # "sphinx": {
        #     "handlers": ["console"],
        #     "level": config('SPHINX_LOG_LVL', default='WARNING'),
        # },
        "": {
            "handlers": ["console"],
            "level": config('APP_LOG_LVL', default='INFO'),
        }
    },
}

# Sentry

# Note that default sentry configuration already includes LoggingIntegration with following
# parameters:
# - level=logging.INFO (captured as breadcrumb)
# - event_level=logging.ERROR (captured as event)
# if we want to sent events from INFO level messages, we need to explicitly redefine
# LoggingIntegration with level=logging.INFO

# DjangoIntegration allows capture django errors as events

sentry_sdk.init(
    dsn=config('SENTRY_DSN'),
    enable_tracing=True,
    integrations=[
        # DjangoIntegration(),
        # LoggingIntegration(
        #  level=logging.INFO,  # Capture info and above as breadcrumbs
        #  event_level=logging.INFO  # Send records as events
        # )
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    traces_sample_rate=1.0,
)
