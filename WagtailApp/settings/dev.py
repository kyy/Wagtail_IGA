from .base import *
from config_reader import config
from db_start import go

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-_&18^x8frjf97mi6+s8=s@c(jfhn6too3a2en8p@op=!2e_hu("

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += [
    "debug_toolbar",
    "django_browser_reload",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

# debug-toolbar / IP адрес, при обращении с которых будет доступен DjDT
INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': go.engine,
        'NAME': go.name,
        'USER': go.user,
        'PASSWORD': config.db_password.get_secret_value(),
        'HOST': 'localhost',
    },
}


try:
    from .local import *
except ImportError:
    pass
