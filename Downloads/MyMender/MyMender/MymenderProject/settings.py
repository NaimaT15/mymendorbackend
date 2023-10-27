from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-qg!qxn=7u9x^xepmuix@hlh_u(5n72nx2vin5wkq$#$-+ap)^c'
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'Auth',
    'Bid',
    'feedback',
    'announcement',
    'services',
    'appointment'
]
CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MymenderProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'MymenderProject.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# DATABASES = {  
#         'default': {  
#             'ENGINE': 'django.db.backends.mysql',  
#             'NAME': 'mymender',  
#             'USER': 'root',  
#             'PASSWORD': 'hanaht123',  
#             'HOST': '127.0.0.1',  
#             'PORT': '3306',  
#             'OPTIONS': {  
#                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
#             }  
#         }  
#     }  
DATABASES = {  
        'default': {  
           'ENGINE': 'django.db.backends.mysql',  
            'NAME': config('DB_NAME'),  
            'USER':  config('DB_USER'),  
            'PASSWORD':  config('DB_USER_PASSWORD'),  
            'HOST':  config('DB_HOST'),  
            'PORT':  config('DB_PORT'),  
            'OPTIONS': {  
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
            }  
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

#AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
#AUTH_USER_MODEL = 'core.User'
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "Auth.serializers.RegistrationSerializer",
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL='Auth.User'
