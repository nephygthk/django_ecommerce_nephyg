import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-4zv=9501^3&75atz(znz(o$_so*n+lnyvon8v6!(m)17y3b02^'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # external applications

    # my project applictions
    'store',
    'cart',
    'account',
    'payment',
    'orders',
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

ROOT_URLCONF = 'core.urls'

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
                'store.context_processors.categories',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = 'account.Customer'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login/'


CART_SESSION_ID = 'cartkey'

# Email setting
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# webhook stripe secret. THIS IS GOTTEN WHEN YOU LOGIN STRIPE WITH CLI
STRIPE_ENDPOINT_SECRET = 'whsec_33c9c43417a6e42a2039e558a81ec80882dba2c6b970abc0f3275bc175d2e210'

STRIP_SECRET_KEY = 'sk_test_51MU42nBCUQwofQ4D0WvmoMh5N9KdpprwO6Obdbkded9Bbii9FQWLeeUfLOJ7gH0xIeRXso7sJJDT55Bsg9ROYmHI00Rk0q2OyT'
STRIP_PUBLIC_KEY = 'pk_test_51MU42nBCUQwofQ4DjrdX8nH2sY34AxEABtNultF87M7zaBs0tehc1mI5vHhSmlDSJ3a0fMLAbJfaxIdGcwu6qYS6005xx3uQic'



# to listen on stripe and forward is = stripe listen --forward-to localhost:8000/payment/webhook/
