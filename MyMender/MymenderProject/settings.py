from pathlib import Path
from decouple import config
from django.urls import reverse_lazy
# from dotenv import load_dotenv
import os
from datetime import timedelta
BASE_DIR = Path(__file__).resolve().parent.parent
# load_dotenv(os.path.join(BASE_DIR, ".env"))
SECRET_KEY = 'django-insecure-qg!qxn=7u9x^xepmuix@hlh_u(5n72nx2vin5wkq$#$-+ap)^c'
DEBUG = True
ALLOWED_HOSTS = []
# DATABASES['default'] =  dj_database_url.config()
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'knox',
    'Auth',
    'rest_framework_simplejwt',
    'Bid',
    'feedback',
    'announcement',
    'Form',
    'services',
    'appointment',
    # 'service',
    'notification',
    'django_filters',
    # 'rest_framework_roles',
    
]
REST_FRAMEWORK_ROLES = {
  'ROLES': 'MymenderProject.roles.ROLES',
}

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
# DATABASES = {  
#         'default': {  
#            'ENGINE': 'django.db.backends.mysql',  
#             'NAME': config('DB_NAME'),  
#             'USER':  config('DB_USER'),  
#             'PASSWORD':  config('DB_USER_PASSWORD'),  
#             'HOST':  config('DB_HOST'),  
#             'PORT':  config('DB_PORT'),  
#             'OPTIONS': {  
#                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
#             }  
#         }  
#     }  

# DB_CONFIG = {"ENGINE": os.getenv("ENGINE"), "NAME": os.getenv("DB_NAME")}

# if DB_CONFIG["ENGINE"] and "mysql" not in DB_CONFIG["ENGINE"]:
#     DB_CONFIG["USER"] = os.getenv("DB_USER") or os.getenv("USER")
#     DB_CONFIG["PASSWORD"] = os.getenv("DB_PASSWORD")
#     DB_CONFIG["HOST"] = os.getenv("DB_HOST")
#     DB_CONFIG["PORT"] = os.getenv("DB_PORT")

# if DB_CONFIG["NAME"] == "db.mysql":
#     DB_CONFIG["NAME"] = os.path.join(BASE_DIR, "db.mysql")

# DATABASES = {"default": DB_CONFIG}

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
REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'Accounts.serializers.LoginUserSerializer',
}
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.SessionAuthentication',
#     ],
# }


CSRF_COOKIE_SECURE=True
CSRF_COOKIE_HTTPONLY=True


# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#         'rest_framework.permissions.DjangoModelPermissions'
#     )
# }
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL='Auth.User'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = ''

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = ''

EMAIL_HOST_PASSWORD = ''
TWILIO_ACCOUNT_SID = 'ACae9c661cbd5ea9e61a23503c0b244db9'
TWILIO_AUTH_TOKEN = 'edc7c2561b3c9b46b51ad6536a784389'

# account_sid = os.environ['ACae9c661cbd5ea9e61a23503c0b244db9']
# auth_token = os.environ['edc7c2561b3c9b46b51ad6536a784389']